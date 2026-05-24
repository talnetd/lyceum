"""Download Coursera 'supplement' assets (PDFs, etc.) for a given course.

Walks a previously-fetched _inbox/<CODE>/course-structure.json, finds supplement
items matching --name-prefix (default: "Programming activity:"), and downloads
each attached asset into _inbox/<CODE>/<assets-dir>/<module-folder>/.

Then mirrors the downloads into courses/<CODE>/practice/programming-activities/
(grouped by topic) for everyday use. Both inbox and curated paths are gitignored.

Usage:
  _tools/.venv/bin/python scripts/fetch-supplements.py <CODE> \
      [--max-module N] [--name-prefix "Programming activity:"]
"""

import argparse
import json
import os
import re
import shutil
import sys
import xml.etree.ElementTree as ET
from http.cookiejar import MozillaCookieJar
from pathlib import Path

import requests

from dl_coursera.define import URL_ROOT, URL_SUPPLEMENT


ASSET_DOWNLOAD = URL_ROOT + "/api/rest/v1/asset/download/{ext}/{aid}"

PART_RE = re.compile(r",?\s*part\s+\d+\s*$", re.IGNORECASE)


def slugify(name, maxlen=80):
    s = name.replace("–", "-").replace("—", "-")
    s = re.sub(r"[^\w\s-]", "", s).strip().lower()
    s = re.sub(r"[-\s]+", "-", s)
    return s[:maxlen] or "untitled"


def base_name(name):
    return PART_RE.sub("", name).strip().rstrip(",").strip()


def parse_assets(cml_value):
    """Extract <asset id="" name="" extension="" /> from supplement CML."""
    try:
        root = ET.fromstring(cml_value)
    except ET.ParseError:
        return []
    return [
        {
            "id": el.get("id"),
            "name": el.get("name") or el.get("id"),
            "extension": (el.get("extension") or "pdf").lower(),
        }
        for el in root.iter("asset")
        if el.get("id")
    ]


def main():
    p = argparse.ArgumentParser()
    p.add_argument("code")
    p.add_argument("--cookies", default="_tools/cookies.txt")
    p.add_argument("--inbox-root", default="_inbox")
    p.add_argument("--course-root", default="courses")
    p.add_argument("--name-prefix", default="Programming activity:")
    p.add_argument("--max-module", type=int, default=None,
                   help="Limit to first N Coursera modules (1-indexed).")
    args = p.parse_args()

    inbox = Path(args.inbox_root) / args.code
    struct_path = inbox / "course-structure.json"
    if not struct_path.exists():
        print(f"ERROR: {struct_path} not found. Run fetch-transcripts.py first.",
              file=sys.stderr)
        sys.exit(1)

    with open(struct_path) as f:
        struct = json.load(f)

    course_id = struct["course"]["id"]
    lessons = {l["id"]: l for l in struct["lessons"]}
    items = {i["id"]: i for i in struct["items"]}
    modules = struct["modules"]
    if args.max_module:
        modules = modules[:args.max_module]

    # Build topic grouping (flatten "..., part N" siblings)
    topic_idx_by_base = {}
    topic_order = []
    for m in modules:
        base = base_name(m["name"])
        if base not in topic_idx_by_base:
            topic_idx_by_base[base] = len(topic_order) + 1
            topic_order.append(base)

    sess = requests.Session()
    cj = MozillaCookieJar()
    cj.load(args.cookies)
    sess.cookies.update(cj)

    assets_inbox_root = inbox / "supplements"
    curated_root = Path(args.course_root) / args.code / "practice" / "programming-activities"
    if curated_root.exists():
        shutil.rmtree(curated_root)
    curated_root.mkdir(parents=True)

    total = 0
    failed = []
    seq_per_topic = {}  # topic_idx -> next seq

    for m_idx, module in enumerate(modules, 1):
        topic_idx = topic_idx_by_base[base_name(module["name"])]
        topic_slug = f"{topic_idx:02d}-{slugify(base_name(module['name']))}"
        for lesson_id in module["lessonIds"]:
            lesson = lessons.get(lesson_id)
            if not lesson:
                continue
            for item_id in lesson["itemIds"]:
                item = items.get(item_id)
                if not item:
                    continue
                if item["contentSummary"]["typeName"] != "supplement":
                    continue
                if not item["name"].startswith(args.name_prefix):
                    continue

                # Fetch supplement payload
                try:
                    r = sess.get(URL_SUPPLEMENT(course_id, item["id"]))
                    r.raise_for_status()
                    payload = r.json()
                except Exception as e:
                    print(f"  ! supplement fetch failed: {item['name']!r}: {e}")
                    failed.append(item["name"])
                    continue

                # Each supplement has 1 'cml' asset wrapper, mine its <asset> children
                cml_blocks = [
                    a for a in payload.get("linked", {}).get("openCourseAssets.v1", [])
                    if a.get("typeName") == "cml"
                ]
                assets = []
                for blk in cml_blocks:
                    val = (blk.get("definition") or {}).get("value", "")
                    if val:
                        assets.extend(parse_assets(val))

                if not assets:
                    print(f"  - no downloadable assets: {item['name']!r}")
                    continue

                # Allocate next sequence number for this topic
                seq_per_topic[topic_idx] = seq_per_topic.get(topic_idx, 0) + 1
                seq = seq_per_topic[topic_idx]
                activity_slug = slugify(item["name"].replace(args.name_prefix, "").strip())

                for a_idx, asset in enumerate(assets, 1):
                    url = ASSET_DOWNLOAD.format(ext=asset["extension"], aid=asset["id"])
                    try:
                        ar = sess.get(url, allow_redirects=True)
                        ar.raise_for_status()
                    except Exception as e:
                        print(f"  ! asset download failed: {asset['name']}: {e}")
                        failed.append(f"{item['name']} -> {asset['name']}")
                        continue

                    # raw filename: try Content-Disposition, else fallback
                    cd = ar.headers.get("Content-Disposition", "")
                    fn_match = re.search(r'filename="?([^"]+)"?', cd)
                    raw_name = fn_match.group(1) if fn_match else \
                               f"{asset['name']}.{asset['extension']}"

                    # Save raw copy under inbox
                    inbox_dir = assets_inbox_root / f"{m_idx:02d}-{slugify(module['name'])}"
                    inbox_dir.mkdir(parents=True, exist_ok=True)
                    inbox_path = inbox_dir / raw_name
                    inbox_path.write_bytes(ar.content)

                    # Save curated copy
                    suffix = f"-{a_idx:02d}" if len(assets) > 1 else ""
                    curated_name = f"{seq:02d}-{activity_slug}{suffix}.{asset['extension']}"
                    curated_dir = curated_root / topic_slug
                    curated_dir.mkdir(parents=True, exist_ok=True)
                    (curated_dir / curated_name).write_bytes(ar.content)

                    total += 1
                    print(f"  + {topic_slug}/{curated_name}  ({len(ar.content)} bytes)")

    print(f"\nDownloaded {total} asset(s).")
    if failed:
        print(f"Failed: {len(failed)}")
        for f in failed:
            print(f"  - {f}")


if __name__ == "__main__":
    main()
