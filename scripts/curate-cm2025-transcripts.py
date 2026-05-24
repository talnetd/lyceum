"""Curate _inbox/CM2025/ transcripts into courses/CM2025/notes/transcripts/.

CM2025 modules are named 'Week N - Topic M: <name> (part K)'. We extract the
Topic number, strip the '(part K)' suffix, and group consecutive modules with
the same topic into a single folder. Lectures renumbered continuously.
"""

import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INBOX = ROOT / "_inbox" / "CM2025"
DEST = ROOT / "courses" / "CM2025" / "notes" / "transcripts"

# 'Week N - Topic M: <base> (part K)' or 'Exam preparation week', 'Exam week'
MODULE_RE = re.compile(
    r"^Week\s+\d+\s*-\s*Topic\s+(\d+)\s*:\s*(.+?)\s*\(?\s*part\s+\d+\s*\)?\s*\)?\s*$",
    re.IGNORECASE,
)


def slugify(name, maxlen=80):
    s = name.replace("–", "-").replace("—", "-")
    s = re.sub(r"[^\w\s-]", "", s).strip().lower()
    s = re.sub(r"[-\s]+", "-", s)
    return s[:maxlen] or "untitled"


def parse(module_name):
    m = MODULE_RE.match(module_name.strip())
    if m:
        return int(m.group(1)), m.group(2).strip().rstrip(":").strip()
    return None, None


def main():
    with open(INBOX / "course-structure.json") as f:
        struct = json.load(f)

    lessons = {l["id"]: l for l in struct["lessons"]}
    items = {i["id"]: i for i in struct["items"]}

    # bucket modules by topic number
    buckets = {}  # topic_num -> list of modules in order
    skipped = []
    for m in struct["modules"]:
        topic, base = parse(m["name"])
        if topic is None:
            skipped.append(m["name"])
            continue
        buckets.setdefault(topic, {"base": base, "modules": []})["modules"].append(m)

    if DEST.exists():
        shutil.rmtree(DEST)
    DEST.mkdir(parents=True)

    summary = []
    for topic_num in sorted(buckets):
        info = buckets[topic_num]
        topic_slug = f"{topic_num:02d}-{slugify(info['base'])}"
        topic_dir = DEST / topic_slug

        seq = 1
        copied = []
        seen_src = set()
        for module in info["modules"]:
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

    if skipped:
        print()
        print(f"Skipped {len(skipped)} non-topic modules:")
        for s in skipped:
            print(f"  - {s}")

    readme = DEST / "README.md"
    lines = [
        "# CM2025 Lecture Transcripts",
        "",
        "Auto-pulled from Coursera via `scripts/fetch-transcripts.py` and curated",
        "by `scripts/curate-cm2025-transcripts.py`. Coursera's 'Week N - Topic M",
        "(part K)' modules are flattened into single topic folders, with lectures",
        "renumbered continuously.",
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
