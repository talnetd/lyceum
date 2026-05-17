"""Download Coursera lecture transcripts (plain-text only) for a given course.

Reuses dl_coursera's URL definitions for the internal Coursera API. Walks the
course's module/lesson/lecture tree and writes each lecture's English
plain-text transcript into a hierarchy under _inbox/<CODE>/.

Usage:
  _tools/.venv/bin/python scripts/fetch-transcripts.py <CODE> <SLUG> [--limit N]
"""

import argparse
import json
import os
import re
import sys
from http.cookiejar import MozillaCookieJar

import requests

from dl_coursera.define import (
    URL_ROOT,
    URL_COURSE_1,
    URL_COURSE_2,
    URL_LECTURE_1,
)


def slugify(name, maxlen=80):
    s = re.sub(r"[^\w\s-]", "", name).strip().lower()
    s = re.sub(r"[-\s]+", "-", s)
    return s[:maxlen] or "untitled"


def get_json(sess, url):
    r = sess.get(url)
    r.raise_for_status()
    return r.json()


def main():
    p = argparse.ArgumentParser()
    p.add_argument("code")
    p.add_argument("slug")
    p.add_argument("--cookies", default="_tools/cookies.txt")
    p.add_argument("--outroot", default="_inbox")
    p.add_argument("--limit", type=int, default=None,
                   help="POC: stop after N transcripts")
    args = p.parse_args()

    sess = requests.Session()
    cj = MozillaCookieJar()
    cj.load(args.cookies)
    sess.cookies.update(cj)

    outdir = os.path.join(args.outroot, args.code)
    os.makedirs(outdir, exist_ok=True)

    d = get_json(sess, URL_COURSE_1(args.slug))
    if "elements" not in d or not d["elements"]:
        print(f"ERROR: course not found for slug={args.slug}", file=sys.stderr)
        print(json.dumps(d, indent=2)[:1000], file=sys.stderr)
        sys.exit(1)
    course = d["elements"][0]
    course_id = course["id"]
    print(f"Course: {course['name']} (id={course_id})")

    d = get_json(sess, URL_COURSE_2(args.slug))["linked"]
    items = {_["id"]: _ for _ in d["onDemandCourseMaterialItems.v2"]}
    lessons = {_["id"]: _ for _ in d["onDemandCourseMaterialLessons.v1"]}
    modules = d["onDemandCourseMaterialModules.v1"]

    with open(os.path.join(outdir, "course-structure.json"), "w") as f:
        json.dump({
            "course": {"id": course_id, "name": course["name"], "slug": args.slug},
            "modules": modules,
            "lessons": list(lessons.values()),
            "items": list(items.values()),
        }, f, indent=2)

    count = 0
    for m_idx, module in enumerate(modules, 1):
        mod_dir = f"{m_idx:02d}-{slugify(module['name'])}"
        for l_idx, lesson_id in enumerate(module["lessonIds"], 1):
            lesson = lessons.get(lesson_id)
            if not lesson:
                continue
            les_dir = f"{m_idx:02d}-{l_idx:02d}-{slugify(lesson['name'])}"
            les_path = os.path.join(outdir, mod_dir, les_dir)

            for i_idx, item_id in enumerate(lesson["itemIds"], 1):
                item = items.get(item_id)
                if not item or item["contentSummary"]["typeName"] != "lecture":
                    continue
                if item.get("isLocked"):
                    continue

                try:
                    ld = get_json(sess, URL_LECTURE_1(course_id, item["id"]))
                except Exception as e:
                    print(f"  ! lecture fetch failed for {item['name']!r}: {e}")
                    continue

                videos = ld.get("linked", {}).get("onDemandVideos.v1", [])
                if not videos:
                    print(f"  - no videos: {item['name']!r}")
                    continue

                for v_idx, video in enumerate(videos, 1):
                    txt_path = (video.get("subtitlesTxt") or {}).get("en")
                    if not txt_path:
                        print(f"  - no en transcript: {item['name']!r} "
                              f"(keys: {list(video.keys())})")
                        continue
                    url_txt = (URL_ROOT + txt_path) if txt_path.startswith("/") else txt_path
                    try:
                        r = sess.get(url_txt)
                        r.raise_for_status()
                    except Exception as e:
                        print(f"  ! transcript fetch failed: {e}")
                        continue

                    os.makedirs(les_path, exist_ok=True)
                    suffix = f"__{v_idx:02d}" if len(videos) > 1 else ""
                    fname = f"{i_idx:02d}-{slugify(item['name'])}{suffix}.txt"
                    fpath = os.path.join(les_path, fname)
                    with open(fpath, "wb") as f:
                        f.write(r.content)
                    print(f"  + {fpath}  ({len(r.content)} bytes)")
                    count += 1
                    if args.limit and count >= args.limit:
                        print(f"\nPOC limit ({args.limit}) reached.")
                        return

    print(f"\nFetched {count} transcripts into {outdir}")


if __name__ == "__main__":
    main()
