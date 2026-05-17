#!/usr/bin/env bash
# Download a Coursera course into _inbox/<CODE>/ via dl_coursera.
#
# Usage:
#   ./scripts/ingest-coursera.sh <COURSE_CODE> <COURSERA_SLUG>
#
# Example:
#   ./scripts/ingest-coursera.sh CM2045 uol-cm2045-professional-practice-for-computer-scientists
#
# Prerequisites:
#   1. Run scripts/install-tools.sh once (or pip install dl-coursera into _tools/.venv).
#   2. Export Coursera cookies from a logged-in browser session into
#      _tools/cookies.txt using a "Get cookies.txt" / "Cookie-Editor" extension
#      (Netscape format). This file is gitignored.

set -euo pipefail

if [[ $# -lt 2 ]]; then
  echo "Usage: $0 <COURSE_CODE> <COURSERA_SLUG>" >&2
  echo "Example: $0 CM2045 uol-cm2045-professional-practice-for-computer-scientists" >&2
  exit 1
fi

CODE="$1"
SLUG="$2"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
VENV_BIN="$ROOT/_tools/.venv/bin"
COOKIES="$ROOT/_tools/cookies.txt"
OUTDIR="$ROOT/_inbox/$CODE"

if [[ ! -x "$VENV_BIN/dl_coursera" ]]; then
  echo "dl_coursera not installed. Run:" >&2
  echo "  python3 -m venv _tools/.venv && _tools/.venv/bin/pip install dl-coursera" >&2
  exit 1
fi

if [[ ! -f "$COOKIES" ]]; then
  echo "Missing $COOKIES" >&2
  echo "Export Coursera cookies from your browser (Netscape format) and save them there." >&2
  exit 1
fi

mkdir -p "$OUTDIR"
echo "Downloading $SLUG into $OUTDIR ..."
"$VENV_BIN/dl_coursera" --cookies "$COOKIES" --outdir "$OUTDIR" "$SLUG"

echo
echo "Done. Raw materials are in $OUTDIR"
echo "Next: curate them into courses/$CODE/{notes,knowledge-base,practice,code,decks}."
