# RPL-IBM-DS: IBM Data Science Professional Certificate

> Non-UoL course pursued for **Recognition of Prior Learning (RPL)**.

## Course info
- **Code:** RPL-IBM-DS
- **Name:** IBM Data Science Professional Certificate
- **Source platform:** Coursera
- **Coursera page:** https://www.coursera.org/professional-certificates/ibm-data-science
- **Status:** In progress

## RPL mapping
- **Maps to UoL module:** **CM2015 Programming with Data** (Level 5)
- **Credit awarded on completion:** 1 x 15 credits
- **Requirement:** Must complete **all 12** sub-courses before applying for RPL with UoL
- **Authoritative source:** [UoL BSc CS RPL page](https://www.london.ac.uk/study/how-apply/recognition-prior-learning/recognition-accreditation-prior-learning-bsc-computer-science)

## Sub-courses (12 total, ~179 hours)

| # | Course | Hours | Status |
|---|---|---|---|
| 01 | What is Data Science? | 12 | **Done** (45 transcripts distilled) |
| 02 | Tools for Data Science | 16 | _Not started_ |
| 03 | Data Science Methodology | 9 | _Not started_ |
| 04 | Python for Data Science, AI & Development | 24 | _Not started_ |
| 05 | Python Project for Data Science | 7 | _Not started_ |
| 06 | Databases and SQL for Data Science with Python | 18 | _Not started_ |
| 07 | Data Analysis with Python | 17 | _Not started_ |
| 08 | Data Visualization with Python | 19 | _Not started_ |
| 09 | Machine Learning with Python | 20 | _Not started_ |
| 10 | Applied Data Science Capstone | 14 | _Not started_ |
| 11 | Generative AI: Elevate Your Data Science Career | 14 | **In progress** (24 transcripts, on lecture 07) |
| 12 | Data Scientist Career Guide and Interview Preparation | 9 | _Not started_ |

## Folders
- [`notes/`](./notes/), per-sub-course distilled notes + `transcripts/<NN-slug>/` per sub-course
- [`knowledge-base/`](./knowledge-base/), atomic concept notes (e.g. `pandas-dataframe.md`, `train-test-split.md`)
- [`practice/`](./practice/), exercises, labs, capstone artefacts
- [`code/`](./code/), notebooks and scripts (one folder per sub-course where useful)
- [`decks/`](./decks/), revision decks / brainstorms

## Workflow per sub-course

1. **Find the Coursera slug** (visible in the URL after `/learn/`).
2. **Pull transcripts:** `_tools/.venv/bin/python scripts/fetch-transcripts.py RPL-IBM-DS <slug>`
3. **Curate** into `notes/transcripts/<NN-sub-course-slug>/` (one folder per sub-course, parallel to CM2040/CM2025 topic flattening).
4. **Distill** into `notes/<NN-sub-course-slug>.md` (style: TL;DR, tables, code, exam fodder).
5. **Update this README** status column from _Not started_ → _In progress_ → _Done_.

## Notes
- Transcripts are gitignored under `courses/*/notes/transcripts/` (UoL-style copyright handling, even though this is IBM/Coursera material).
- Programming activity PDFs (if any) get gitignored under `courses/*/practice/programming-activities/`.
- The CM2015 RPL is "all or nothing", partial completion doesn't earn partial credit.

## Resources
- IBM Skills Network: https://skills.network/
- Cert overview: https://www.coursera.org/professional-certificates/ibm-data-science
