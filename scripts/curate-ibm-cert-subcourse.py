"""Curate one IBM-cert sub-course inbox into courses/<PARENT>/notes/transcripts/<NN-slug>/.

IBM Coursera sub-courses are single-module-per-week (no Part 1/Part 2 splits),
so this just flattens the inbox lecture files into a numbered list under one
target folder.

Usage:
  _tools/.venv/bin/python scripts/curate-ibm-cert-subcourse.py \
      --inbox _inbox/RPL-IBM-DS-11-genai \
      --parent RPL-IBM-DS \
      --target 11-generative-ai-elevate-your-data-science-career
"""

import argparse
import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def slugify(name, maxlen=80):
    s = name.replace("–", "-").replace("—", "-")
    s = re.sub(r"[^\w\s-]", "", s).strip().lower()
    s = re.sub(r"[-\s]+", "-", s)
    return s[:maxlen] or "untitled"


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--inbox", required=True, help="Inbox dir, e.g. _inbox/RPL-IBM-DS-11-genai")
    p.add_argument("--parent", required=True, help="Parent course code, e.g. RPL-IBM-DS")
    p.add_argument("--target", required=True, help="Target sub-folder, e.g. 11-genai-...")
    args = p.parse_args()

    inbox = Path(args.inbox)
    with open(inbox / "course-structure.json") as f:
        struct = json.load(f)

    lessons = {l["id"]: l for l in struct["lessons"]}
    items = {i["id"]: i for i in struct["items"]}
    modules = struct["modules"]

    dest = ROOT / "courses" / args.parent / "notes" / "transcripts" / args.target
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir(parents=True)

    seq = 1
    copied = []
    seen_src = set()

    for m_idx, module in enumerate(modules, 1):
        mod_slug = slugify(module["name"])
        candidates = list(inbox.glob(f"*-{mod_slug}"))
        if not candidates:
            continue
        mod_dir = candidates[0]

        for lesson_id in module["lessonIds"]:
            lesson = lessons.get(lesson_id)
            if not lesson:
                continue
            for item_id in lesson["itemIds"]:
                item = items.get(item_id)
                if not item or item["contentSummary"]["typeName"] != "lecture":
                    continue
                lecture_slug = slugify(item["name"])
                matches = sorted(
                    p for p in mod_dir.rglob("*.txt")
                    if re.match(
                        rf"\d+-{re.escape(lecture_slug)}(?:__\d+)?\.txt$",
                        p.name,
                    )
                )
                for src in matches:
                    if src in seen_src:
                        continue
                    seen_src.add(src)
                    m = re.search(r"(__\d+)\.txt$", src.name)
                    suffix = m.group(1) if m else ""
                    dest_name = f"{seq:02d}-{lecture_slug}{suffix}.txt"
                    shutil.copy2(src, dest / dest_name)
                    copied.append(dest_name)
                    seq += 1

    print(f"{args.target}: {len(copied)} transcripts")


if __name__ == "__main__":
    main()
