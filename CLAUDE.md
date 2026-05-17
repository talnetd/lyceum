# Lyceum — Study System for UOL BSc CS

> Codenamed after **Lyceum**, Aristotle's school in Athens.

This repo is the user's personal study system for the online University of London BSc Computer Science programme. All academic work — notes, knowledge base entries, practice problems, code, slide decks — is organized **per course**.

## Repository layout

```
lyceum/
├── CLAUDE.md                  # this file
├── README.md                  # course index (human-facing)
├── .gitignore
├── courses/
│   └── <COURSE_CODE>/         # e.g. CM2045, CM1010, CM2005
│       ├── README.md          # course metadata: full name, term, status, syllabus link
│       ├── notes/             # lecture notes, weekly summaries (Markdown)
│       ├── knowledge-base/    # atomic concept notes (one idea per file, Zettelkasten-style)
│       ├── practice/          # exercises, problem sets, past papers
│       ├── code/              # code snippets, mini-projects, lab solutions
│       └── decks/             # slide decks, brainstorms, mind-maps
├── shared/                    # cross-course resources (cheatsheets, study habits, glossary)
└── scripts/
    └── new-course.sh          # scaffold a new course folder
```

## Course naming convention

Folder name = the UOL course code (e.g. `CM2045`). The human-readable course name and other metadata live in `courses/<CODE>/README.md`. This keeps folder names short and scriptable while preserving full course information.

## File naming conventions

- **Notes:** `week-NN-topic.md` (e.g. `week-03-recursion.md`) — zero-padded so they sort naturally.
- **Knowledge base:** kebab-case concept names (e.g. `big-o-notation.md`, `tcp-handshake.md`). One concept per file. Link related concepts with `[[wiki-style]]` links — even if the target doesn't exist yet (that's a TODO marker).
- **Practice:** `problem-set-NN.md` or `past-paper-YYYY.md`.
- **Code:** mirror the topic structure. Use the language's idiomatic project layout (e.g. `pyproject.toml` for Python, `package.json` for Node).
- **Decks:** `YYYY-MM-DD-title.pptx` or `.md` for outlines.

## Workflows

### Adding a new course
Run `./scripts/new-course.sh CM2045 "Programming with Python"` from the repo root. It creates the folder skeleton and pre-fills the course README.

### Adding study materials
- Drop notes into `courses/<CODE>/notes/`.
- For a concept worth remembering across courses, also add a `knowledge-base/` entry — it's the long-term memory; lecture notes are the short-term capture.

### Generating slide decks
The `enterprise-pptx` skill (Claude Code) can build polished .pptx decks from outlines — useful for revision summaries or study group presentations. Outlines live as Markdown in `decks/`, generated `.pptx` files alongside.

### Committing
- Scope commits per course: `CM2045: add week 3 recursion notes`.
- Cross-cutting changes: `shared: add Big-O cheatsheet`.

## What goes where — quick reference

| You want to save... | Put it in... |
|---|---|
| A lecture summary | `courses/<CODE>/notes/` |
| A reusable concept explanation | `courses/<CODE>/knowledge-base/` (or `shared/` if course-agnostic) |
| A coursework solution | `courses/<CODE>/code/` |
| A past paper attempt | `courses/<CODE>/practice/` |
| A revision slide deck | `courses/<CODE>/decks/` |
| A study habit / planner | `shared/` |

## Tracking on GitHub

This repo is meant to be pushed to a private GitHub repo. Don't commit anything that violates UOL's academic integrity policy (e.g. don't publicly publish in-progress assessed coursework). Keep the repo **private** while a course is active.
