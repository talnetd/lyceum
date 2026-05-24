"""Curate _inbox/CM2040/ transcripts into courses/CM2040/notes/transcripts/.

CM2040 modules are named like 'Building web apps with Node and Express, part 1',
'..., part 2', '..., part 3'. We strip the ', part N' suffix to group consecutive
modules into a single topic, renumber lectures continuously, and slugify.
"""

import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INBOX = ROOT / "_inbox" / "CM2040"
DEST = ROOT / "courses" / "CM2040" / "notes" / "transcripts"

PART_RE = re.compile(r",?\s*part\s+\d+\s*$", re.IGNORECASE)


def slugify(name, maxlen=80):
    s = name.replace("–", "-").replace("—", "-")
    s = re.sub(r"[^\w\s-]", "", s).strip().lower()
    s = re.sub(r"[-\s]+", "-", s)
    return s[:maxlen] or "untitled"


def base_name(module_name):
    return PART_RE.sub("", module_name).strip().rstrip(",").strip()


def main():
    with open(INBOX / "course-structure.json") as f:
        struct = json.load(f)

    lessons = {l["id"]: l for l in struct["lessons"]}
    items = {i["id"]: i for i in struct["items"]}

    # Group modules into topics by base name, preserving order
    topics = []  # list of (base_name, [module, ...])
    by_base = {}
    for m in struct["modules"]:
        base = base_name(m["name"])
        if base not in by_base:
            by_base[base] = []
            topics.append((base, by_base[base]))
        by_base[base].append(m)

    if DEST.exists():
        shutil.rmtree(DEST)
    DEST.mkdir(parents=True)

    summary = []
    for topic_idx, (base, modules) in enumerate(topics, 1):
        topic_slug = f"{topic_idx:02d}-{slugify(base)}"
        topic_dir = DEST / topic_slug

        seq = 1
        copied = []
        seen_src = set()
        for module in modules:
            # locate the inbox module directory by its slugified name
            mod_slug = slugify(module["name"])
            candidates = list(INBOX.glob(f"*-{mod_slug}"))
            if not candidates:
                continue
            mod_dir_inbox = candidates[0]

            for lesson_id in module["lessonIds"]:
                lesson = lessons.get(lesson_id)
                if not lesson:
                    continue
                for item_id in lesson["itemIds"]:
                    item = items.get(item_id)
                    if not item or item["contentSummary"]["typeName"] != "lecture":
                        continue
                    lecture_slug = slugify(item["name"])
                    # Anchor: filename is "NN-{slug}.txt" or "NN-{slug}__NN.txt"
                    matches = sorted(
                        p for p in mod_dir_inbox.rglob("*.txt")
                        if re.match(
                            rf"\d+-{re.escape(lecture_slug)}(?:__\d+)?\.txt$",
                            p.name,
                        )
                    )
                    if not matches:
                        continue
                    for src in matches:
                        if src in seen_src:
                            continue
                        seen_src.add(src)
                        if not topic_dir.exists():
                            topic_dir.mkdir()
                        m = re.search(r"(__\d+)\.txt$", src.name)
                        suffix = m.group(1) if m else ""
                        dest_name = f"{seq:02d}-{lecture_slug}{suffix}.txt"
                        shutil.copy2(src, topic_dir / dest_name)
                        copied.append(dest_name)
                        seq += 1

        if copied:
            print(f"{topic_slug}: {len(copied)} transcripts")
            summary.append((topic_slug, copied))
        else:
            print(f"{topic_slug}: (no transcripts, skipping)")

    readme = DEST / "README.md"
    lines = [
        "# CM2040 Lecture Transcripts",
        "",
        "Auto-pulled from Coursera via `scripts/fetch-transcripts.py` and curated",
        "by `scripts/curate-cm2040-transcripts.py`. Coursera's part-1/2/3 module",
        "splits are flattened into single topic folders, with lectures renumbered",
        "continuously in delivery order.",
        "",
        "## Topics",
        "",
    ]
    for topic_slug, copied in summary:
        lines.append(f"- [`{topic_slug}/`](./{topic_slug}/), {len(copied)} lectures")
    lines.append("")
    readme.write_text("\n".join(lines))


if __name__ == "__main__":
    main()
