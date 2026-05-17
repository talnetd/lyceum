# Lyceum

> _Codenamed after Aristotle's school._

Personal study system for the University of London online BSc Computer Science programme. Organized per course; tracked on GitHub.

See [`CLAUDE.md`](./CLAUDE.md) for the layout, conventions, and workflows.

## Courses

| Code | Name | Term | Status |
|---|---|---|---|
| [CM2045](./courses/CM2045/) | _(fill in)_ | _(e.g. Apr 2026)_ | In progress |

> Add a new course: `./scripts/new-course.sh <CODE> "<Full Name>"`

## Shared resources

- [`shared/`](./shared/) — cross-course cheatsheets, study habits, glossary.

## Getting started

```bash
git init
git add .
git commit -m "Initial commit: Lyceum scaffold"
gh repo create lyceum --private --source=. --remote=origin --push
```
