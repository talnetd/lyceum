#!/usr/bin/env bash
# Scaffold a new course folder under courses/.
#
# Usage:
#   ./scripts/new-course.sh <COURSE_CODE> "<Full Course Name>"
#
# Example:
#   ./scripts/new-course.sh CM2045 "Programming with Python"

set -euo pipefail

if [[ $# -lt 2 ]]; then
  echo "Usage: $0 <COURSE_CODE> \"<Full Course Name>\"" >&2
  exit 1
fi

CODE="$1"
NAME="$2"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DIR="$ROOT/courses/$CODE"

if [[ -d "$DIR" ]]; then
  echo "Course folder already exists: $DIR" >&2
  exit 1
fi

mkdir -p "$DIR"/{notes,knowledge-base,practice,code,decks}

# Per-folder .gitkeep so empty dirs are tracked
for sub in notes knowledge-base practice code decks; do
  touch "$DIR/$sub/.gitkeep"
done

cat > "$DIR/README.md" <<EOF
# $CODE: $NAME

## Course info
- **Code:** $CODE
- **Name:** $NAME
- **Term:** _(e.g. April 2026 sitting)_
- **Status:** In progress
- **Syllabus / module page:** _(link)_

## Assessment
- _(coursework weighting, exam format, deadlines)_

## Folders
- [\`notes/\`](./notes/), weekly lecture notes
- [\`knowledge-base/\`](./knowledge-base/), atomic concept notes
- [\`practice/\`](./practice/), exercises and past papers
- [\`code/\`](./code/), code snippets and mini-projects
- [\`decks/\`](./decks/), slide decks and brainstorms

## Topics covered
- _(fill in as the term progresses)_

## Resources
- _(textbooks, lecturer notes, useful links)_
EOF

echo "Created $DIR"
echo "  + notes/ knowledge-base/ practice/ code/ decks/"
echo "  + README.md"
echo
echo "Next: edit $DIR/README.md to fill in term and syllabus link."
