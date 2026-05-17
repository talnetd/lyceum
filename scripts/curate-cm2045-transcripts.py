"""Curate _inbox/CM2045/ transcripts into courses/CM2045/notes/transcripts/.

Flattens Coursera's Part 1 / Part 2 module split into 10 topic folders, with
lectures renumbered continuously per topic in their original order.
"""

import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INBOX = ROOT / "_inbox" / "CM2045"
DEST = ROOT / "courses" / "CM2045" / "notes" / "transcripts"

TOPIC_SLUGS = {
    1: "01-written-communication",
    2: "02-presentation-public-speaking",
    3: "03-legal-ethical-foundations",
    4: "04-inclusive-computing",
    5: "05-sustainability",
    6: "06-risk-security",
    7: "07-industry-standards",
    8: "08-teamwork-collaboration",
    9: "09-project-management",
    10: "10-professional-development",
}


def parse_module(name):
    m = re.match(r"Topic\s+(\d+):\s*(.+?)(?:,\s*Part\s+(\d+))?\s*$", name.strip())
    if not m:
        return None, None
    return int(m.group(1)), int(m.group(3) or 1)


def main():
    with open(INBOX / "course-structure.json") as f:
        struct = json.load(f)

    lessons = {l["id"]: l for l in struct["lessons"]}
    items = {i["id"]: i for i in struct["items"]}

    # bucket modules by topic, ordered by part
    buckets = {}  # topic_num -> list of (part, module)
    for m in struct["modules"]:
        topic, part = parse_module(m["name"])
        if topic is None:
            print(f"skipping unparseable module: {m['name']!r}")
            continue
        buckets.setdefault(topic, []).append((part, m))

    if DEST.exists():
        shutil.rmtree(DEST)
    DEST.mkdir(parents=True)

    summary = []
    for topic_num in sorted(buckets):
        topic_slug = TOPIC_SLUGS[topic_num]
        topic_dir = DEST / topic_slug
        topic_dir.mkdir()

        seq = 1
        copied = []
        for part, module in sorted(buckets[topic_num]):
            mod_dir_inbox = next(INBOX.glob(f"*-topic-{topic_num}-*part-{part}*"), None)
            if not mod_dir_inbox:
                # fall back to module name slug
                continue
            for lesson_id in module["lessonIds"]:
                lesson = lessons.get(lesson_id)
                if not lesson:
                    continue
                for item_id in lesson["itemIds"]:
                    item = items.get(item_id)
                    if not item or item["contentSummary"]["typeName"] != "lecture":
                        continue
                    lecture_slug = re.sub(r"[^\w\s-]", "", item["name"]).strip().lower()
                    lecture_slug = re.sub(r"[-\s]+", "-", lecture_slug)[:80] or "untitled"

                    # find source file inside the module dir (could be in any lesson subdir)
                    matches = list(mod_dir_inbox.rglob(f"*{lecture_slug}*.txt"))
                    if not matches:
                        print(f"  ! no transcript file for {item['name']!r}")
                        continue
                    src = matches[0]
                    dest_name = f"{seq:02d}-{lecture_slug}.txt"
                    shutil.copy2(src, topic_dir / dest_name)
                    copied.append(dest_name)
                    seq += 1

        print(f"{topic_slug}: {len(copied)} transcripts")
        summary.append((topic_slug, copied))

    # write a README for the transcripts folder
    readme = DEST / "README.md"
    lines = [
        "# CM2045 Lecture Transcripts",
        "",
        "Auto-pulled from Coursera via `scripts/fetch-transcripts.py` and curated by",
        "`scripts/curate-cm2045-transcripts.py`. The 20 Coursera modules (10 topics x",
        "Part 1/Part 2 pacing) are flattened into 10 topic folders, with lectures",
        "renumbered continuously in delivery order.",
        "",
        "## Topics",
        "",
    ]
    for topic_slug, copied in summary:
        lines.append(f"- [`{topic_slug}/`](./{topic_slug}/) — {len(copied)} lectures")
    lines.append("")
    readme.write_text("\n".join(lines))


if __name__ == "__main__":
    main()
