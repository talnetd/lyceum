# Topic 1: Written Communication

> CM2045 · Topic 1 (Written Communication) · 11 lectures
> Source transcripts: `notes/transcripts/01-written-communication/` (local, gitignored)

## TL;DR
CM2045 (Professional Practice for Computer Scientists, a **Level 5** module, ~**150 notional hours**) builds three career pillars: **communication**, **ethical responsibility**, and **continuous professional development**. Topic 1 is the communication foundation, and its through-line is **audience and purpose**: good writing is **clear, concise, accurate, well-organised, and objective**, with terminology defined on first use and structure no more than ~four headings deep. The signature professional skill is **distillation**, taking complex inputs (a 177-page **PhD thesis**, 300-to-500-page ethnographic field reports, dense **programme regulations**) and compressing them into accessible **summaries, tables, and figures**. You read research efficiently (**abstract → evaluation/conclusion → introduction → full paper**), structure your own writing the same way (abstract, headings/subheadings, table of figures/tables, per-section summaries that lead into the next section), and lean on the two core visual forms (**tables for X-vs-Y comparison**, **figures for interrelated concepts**). The topic also previews oral/pitch communication evaluated by **heuristics**, the **nine communication styles**, and **assertive communication** for careers (think-like-the-recruiter, evidence-backed, with the **STAR(R)** framework). Recurring named authorities: usability pioneers **Jakob Nielsen, Donald Norman, Ben Shneiderman**.

## 1. The module in context ([[professional-practice-overview]])

Lecturer: **Dr Sean McGrath** (Goldsmiths / University of London). The module sits above Level 4 introductory modules, so expect more reading and independent thinking.

- **Three pillars:** effective communication, ethical responsibility, continuous professional development.
- **Five structured areas:** (1) foundations of professional practice, (2) communication skills (written, verbal, visual), (3) ethical/legal/sustainability considerations, (4) teamwork and project management (including **agile**), (5) career planning and lifelong learning.
- **Why it matters:** employers want more than code; they value people who can communicate to technical *and* non-technical audiences, work in teams, manage projects, and reason about ethics.
- **Assessment:** several components including a **reflective** element; activities build a **portfolio** that feeds the final assessment. There is a **midterm coursework** at the module's midpoint. (likely exam fodder: the module is **assessed partly on your writing/communication**, unusual for a CS module.)
- The content here is "contentious and subjective", different from the deterministic feel of algorithm design.

## 2. What technical writing is ([[technical-writing]])

**Technical writing** = communicating complex information **clearly and effectively to a specific audience**. It is not storytelling or personal style; it is about the reader understanding the information.

### The five qualities of good technical writing (likely exam fodder)
| Quality | What it means | Practical rule |
|---|---|---|
| **Clarity** | Reader must understand the message | Simple language; avoid jargon, or define it; a **glossary** helps |
| **Concise** | Communicate as efficiently as possible | Mostly simple sentences, a few compound/complex ones to break monotony |
| **Accurate** | One mistake causes misunderstanding/errors | Double-check facts, figures, instructions (e.g. 150 vs 1,500 hours) |
| **Well-organised** | Easy to follow and navigate | Headings, subheadings, bullets, numbered lists |
| **Objective / neutral** | Present facts, not opinions | "I prefer dogs to cats" is fine; "dogs are better than cats" needs evidence |

- **Abbreviations:** define on **first use**.
- **Heading depth heuristic:** go about **four subheadings deep** before it gets confusing. Mnemonic: like an IP address, `1.1.1.1.1` is invalid. (likely exam fodder)
- Opinions are allowed (with evidence) only in discussion/evaluation sections, backed by **rigorous empirical evidence**.

### Why it matters in CS
Clear documentation bridges developers, engineers, and non-technical stakeholders; saves time on onboarding/troubleshooting; prevents costly mistakes; and differentiates candidates in the job market (careers exist in **publishing** and **UX**).

### Common types of technical writing
| Type | Audience / purpose |
|---|---|
| **User manuals & guides** | End users; e.g. Unix **man pages**, language docs |
| **API documentation** | Developers; requests, responses, configs, dependencies |
| **Technical reports** | Specific audience; findings, recommendations, milestones |
| **Code comments** | Other developers; short for complex tasks, longer for complex algorithms (Python **docstrings** are the exemplar) |
| **White papers & research papers** | Highly technical; novel research/findings (note: transcript also calls these "plug strings", read as docstrings) |

### The writing process (5 steps)
1. **Know your audience** (experts vs non-technical stakeholders): tailor depth and jargon. "Better to speak to a million people than one person."
2. **Define the purpose** (instruct, explain, summarise). Research often opens with a **literature review** before the novel contribution emerges.
3. **Organise logically** (headings, bullets, diagrams; most-important-first). McGrath uses **sticky notes**, grouped into themes, folded into simpler constructs.
4. **Write** (intro overview, then structured body; start with bullets/tables, then expand).
5. **Review** (clarity, conciseness, accuracy) and get feedback; **peer review** is the quality check for manuscripts.

### Tooling
- **Markdown / LaTeX** for formatting (UoL exam scripts use LaTeX; HTML/markup is the same "semantic structure" idea).
- **AI tools** for grammar/style/readability (Python NLP libraries can help rewrite). Caveat below.
- Graphics software for flowcharts/diagrams; API doc generators.

## 3. Distilling a dense document: summarising programme regulations ([[summarising-regulations]])

**Programme regulations** = the rules, requirements, and guidelines defining how your degree is structured. They cover modules per pathway, **credit requirements**, **assessment criteria**, and **conditions to repeat/withdraw** (e.g. a grade of **20%**). They are "technical" but not tied to a technology, and they vary widely between institutions (McGrath has worked at **seven** universities).

Why they matter: clarity (a roadmap), navigating challenges (reassessment, special circumstances), setting expectations (deadlines, **academic integrity**), and supporting fairness/success. Rules bind staff as much as students; expectations must be **reasonable on both sides**.

### The summarisation exercise (a technical-writing practice task)
- **Skim first** for structure: module requirements, assessment policies, progression rules, special circumstances/appeals.
- **Identify the essentials** a new student needs: core vs optional modules (what and when), assessment/pass marks, progression rules, reassessment/retake policies.
- **Write clearly and objectively** with headings and bullets; no opinions or advice.
- **Format:** aim for **~two pages**, a quick-reference guide readable in a few minutes; consider whether it collapses into a **single table**. Can become part of your **portfolio**.
- **Caution on text summarisers / LLMs:** McGrath asked a popular LLM a regulations question; it gave incorrect info, and when challenged it **doubled down and "lied"**. Useful tools, but **do not over-trust them**. (likely exam fodder: verify AI output against ground truth.)

## 4. Reading and structuring a technical report ([[anatomy-of-a-technical-document]])

Worked example: McGrath's own **PhD thesis** (**~177 pages**, a 3-year body of work). A PhD = **three independent (often published) studies** linked by a **narrative/rhetoric**, plus a **discursive element** on impact. Each chapter can be read as a standalone paper.

### How to read research efficiently (likely exam fodder)
Read **strategically, not linearly**, to decide relevance fast and avoid wasting a day on an irrelevant 177-page read:
1. **Abstract** first: summarises the research without citations; skim for keywords (tools, methods, themes like user satisfaction) to judge relevance.
2. **Evaluation / conclusion** next: strengths, limitations, key outcomes.
3. **Introduction** (quick skim).
4. **Full paper**, only if still relevant.

### Anatomy / information architecture
A document is like a website's navigation: it needs structure so readers can find what they want.
| Element | Role |
|---|---|
| Title, author, institution | Identification |
| **Abstract** | Standalone summary, first thing a reader reads |
| **Table of figures** + **table of tables** | Navigate the key outcomes (often the most valuable, X-vs-Y, content) |
| **Chapters** with numbered headings/subheadings | Hierarchical structure |
| **Introduction / literature review** | Look back at prior work (**Nielsen, Norman, Shneiderman**, 1990s usability) to frame and substantiate the novel contribution |
| **Methodology / methods** | "Recipe": step-by-step process so research is **replicable**; metric-driven (e.g. **open coding** to fold themes into an ontology) |
| **Empirical chapters** | The studies themselves; deeper nesting (3.1.1) as detail increases |
| **Discussion / evaluation** | Connect the dots, broader implications |

### Structuring your own writing (advice)
- **Match heading depth to discussion depth:** shallow intro = ~2 levels; theme-rich literature/methods chapters = ~3 levels (3.1.1).
- **Per-section summaries that flow into the next section**, not just one summary at the end, to give the document **emergent flow** ("this is what we found, here is where we go next").
- For early-career writers: write a **formal literature review chapter early** and create citations as you go so you can refer back.
- The scientific arc: study X + study Y → enables novel investigation Z = an **original contribution**.
- Shorter formats also exist: **works-in-progress / short papers** (1-2 pages) for a single new discovery; length tracks how contemporary the topic is.

## 5. Integrating visual aids: turning complexity into meaning ([[visual-aids-data-visualisation]])

Context: the **FAST project** (Fusing Audio and Semantic Technologies), **~£6m**, funded by **EPSRC**, with multiple universities and industry partners, studying music-making/production practice to find design opportunities. (En-dash range example for reference only.)

**The core problem:** **field reports** carry **high volume + high complexity**; raw qualitative data still **lacks meaning**. You must capture everything in situ, then decide later what is useful, then **translate** it into something a designer/developer can act on, and verify it is **generalisable** (more than one use case), not a single anecdote.

### What you look for in field reports
- **Existing best practice** to emulate (e.g. blue underlined hyperlinks; do not reinvent the wheel).
- **Opportunities for improvement** of existing processes.
- **Opportunities for innovation** (the **novelty proposition**, e.g. a robot that auto-positions a microphone).

### Two dimensions to capture (the driving analogy)
| Dimension | Diagram type | Driving analogy |
|---|---|---|
| **Actions and intents** | use case / activity diagram (agile **user stories**) | mirror, signal, manoeuvre; press accelerator with intent to speed up |
| **State of the process** | sequence diagram | where you are, destination, ETA, restrictions |

### The distillation pipeline (likely exam fodder)
Boil thousands of pages down to meaning, step by step:
1. **Map** two axes against each other in a **table (X-vs-Y)**: e.g. **concerns/preoccupations (coded O3, O4...)** vs **practices (coded P3, P16, P17, P19, P29...)**, across project stages.
2. **Generalise / code:** group common behaviours; apply a **coding scheme**, **colour**, and a **numerical scheme**.
3. **Abstract to stages:** collapse to high-level phases, **pre-production → production → post-production → delivery**, reducing thousands of pages to ~**five steps**.
4. **Drill back down** into each phase only where design interventions are needed.

A short participant **quote** (verse-writing "like a puzzle") shows how a small piece of qualitative data reveals structure, intent, and design implications.

**Research output example, the "digital music object":** music is not a static, one-off composition but a **digital artifact** that evolves over its lifecycle (sheet music → recording → remix → acoustic version → remix of the remix), with rich **metadata**. Three categories of action emerged: **tagging/indexing/linking** (storable/retrievable), **provenancing/ownership** (signing the sound, branding, copyright/**IP**), and **reusability**.

### Takeaway: the two visual workhorses
- **Tables** = X-vs-Y comparison, mapping one thing against others (great for complexity in systems).
- **Figures** = visual structures for **interrelated concepts**.
Use both heavily to make factual/descriptive writing accessible. (likely exam fodder.)

## 6. Design heuristics ([[design-heuristics]])

**Design heuristics** = broad, flexible guidelines (not rigid rules) for building usable systems; they serve **both design and evaluation**. You can write heuristics for almost anything (even an **ISO standard** for making tea exists). Classic examples: **consistency and standards**, **error prevention**. Authorities again: **Nielsen, Norman, Shneiderman** (general-case heuristics).

Worked example: usability of **Digital Audio Workstations (DAWs)**, notoriously complex/cluttered software. Method: **workshops and focus groups** with professionals split into three roles.

| Role | Focus | Priority |
|---|---|---|
| **Performers** | Live performance / composition | Flexibility, creative freedom |
| **Producers** | Indoor editing, mixing, arranging | Efficient workflows |
| **Agents** | Managers / label reps supporting production | Stakeholder support |

Roles are **dynamic** (they shift through a project), best shown later as a **Venn / concept diagram**, a reminder that complex visuals can be made accessible.

### Mapping usability problems to heuristics
| Usability problem | Heuristic that addresses it |
|---|---|
| **Too much control** (clutter, too many features) | **Efficiency** (streamlined interface) |
| **Poor workflow** (cannot see where you are) | Workflow visibility |
| **Unclear metaphors/symbols** (icons unlike real instruments) | Match real-world conventions |
| **Inconsistent controls** | **Consistency** |

Participant solutions: real-time collaboration/direct commenting, **one-click** functionality to cut cognitive load, filtering to find tracks. A heuristics table is essentially a **lookup**, often with **severity numbers** and **colours** for prevalence.

**Trade-off principle (likely exam fodder):** software design is almost always a trade-off; you rarely get the best of both worlds and instead make **incremental improvements**. Context sets the priority: **efficiency** in a financial trading system (seconds = millions), **effectiveness** over speed in scientific applications. *Reflection* on the activity matters as much as the output.

## 7. Oral / pitch communication and self-assessment ([[pitch-presentation-heuristics]])

The rules for spoken presentation mirror written ones; you can even script and follow along. Presentations (e.g. a **mobile app pitch**) are evaluated by **content** and **style** heuristics.

| Dimension | Heuristics |
|---|---|
| **Content** | **Logical flow** (pain point → features → impact); **simplicity & focus** (clear value proposition); **audience appropriateness** (features for technical, UX/business for non-technical) |
| **Style / delivery** | **Confidence & enthusiasm** (sell your belief, not just the app); **clear, concise** language (mind pace, avoid jargon); **visual aids** that enhance not distract (clean, focused; the **A1 poster** worked because of colourful flow + visuals); **audience interaction** (eye contact, questions, checking understanding) |

**TED Talks** are the model: abstract ideas presented to spark curiosity. Goal: make the message **clear, engaging, and memorable**.

## 8. The nine communication styles ([[communication-styles]])

No one-size-fits-all; choose by situation, audience, and goal. (likely exam fodder: be able to name and match these.)

| # | Style | When to use | Key tactic |
|---|---|---|---|
| 1 | **Firm but fair** | Setting expectations, accountability | Clear + direct + consistent; constructive feedback; firm ≠ harsh |
| 2 | **Assertive** | Honest, respectful self-expression | **"I" statements** ("I need this by Monday" vs "you always delay"); active listening |
| 3 | **Empathetic** | Sensitive/emotional situations | Acknowledge feelings; offer support; build trust |
| 4 | **Collaborative** | Team/group decisions | Encourage participation; **consensus building**; ensure everyone feels heard |
| 5 | **Direct and decisive** | Time-pressured, clear leadership | Communicate without ambiguity; take responsibility; confidence |
| 6 | **Persuasive** | Pitching ideas, seeking buy-in | **Logic + emotion + credibility** |
| 7 | **Supportive** | Motivating/encouraging others | Encouragement, availability, resources |
| 8 | **Adaptable** | Fast-changing or diverse contexts | Know audience; flex between styles; monitor and adjust |
| 9 | **Diplomatic** | Conflict / sensitive negotiation | Careful word choice; stay neutral; build bridges |

## 9. Assertive communication for your career ([[assertive-communication]])

Presenter: **Liz Wilkinson**, Senior Careers Consultant, **University of London Career Service**.

**Assertive communication** = the **middle way between passive and aggressive** (what counts as assertive varies by **cultural context**). It improves every phase of job hunting: networking, shortlisting, interview persuasiveness, and **salary negotiation**, a strong **return on investment**. Employers prize it because assertive communicators improve **financial performance and viability** (teamwork, conflict resolution, briefing managers, handling customers/stakeholders/investors).

### Three elements of assertive communication (likely exam fodder)
1. **Understand the reader/audience's priorities** (what they care about, worry about).
2. **Marshal relevant facts and evidence** to support your argument.
3. **A clear, relevant line of argument**, often with a **positive next step** to move things forward.

Links to UoL's **10 global employability skills** (communication is one; **persuasion and negotiation** another), framed as the **human advantage in an AI-enriched environment**.

### AI caveat for CVs
AI improves clarity, spelling, grammar, and targeting, but recruiters now complain of **too many bland, over-generalised AI CVs**. Only a **human** can judge what convinces another human and match your specific experience to the role, so always re-read and add a **personalised touch**.

### Writing an assertive CV/application
- **Think like the recruiter:** what problem is the job created to solve? What do they need reassurance about (will the hire stay, deliver to spec/deadline, fit the team, have a work ethic)?
- **Back statements with evidence** of both technical and global employability skills; show **results and impact**.
- **Check clarity and relevance:** re-read the job description and the org's website; is it obvious you are applying for *this* job?

### The STAR(R) framework (likely exam fodder)
| Letter | Meaning |
|---|---|
| **S** | Situation (brief description) |
| **T** | Task you tackled |
| **A** | Actions you took, the **biggest section**, 4-5 strong verbs |
| **R** | Results / positive business impact |
| **R** | Reflection: what you learned, what you would do differently |

UoL Career Service resources: webinars, guidelines, AI-enhanced CV tools, and a **global employability skills micro-module** with a technical-communication section.

## Related concepts
- [[technical-writing]], the five qualities (clear, concise, accurate, organised, objective) and the writing process
- [[anatomy-of-a-technical-document]], abstract → evaluation → intro → full paper; structuring your own
- [[summarising-regulations]], distilling a dense document into a 2-page quick reference
- [[visual-aids-data-visualisation]], the field-report distillation pipeline; tables vs figures
- [[design-heuristics]], flexible usability guidelines; problem-to-heuristic mapping; trade-offs
- [[communication-styles]], the nine styles and when to use each
- [[assertive-communication]], the passive/assertive/aggressive spectrum and its three elements
- [[star-method]], STAR(R) framework for application statements, TODO
- [[global-employability-skills]], UoL's 10 in-demand skills, TODO
- [[usability-pioneers]], Nielsen, Norman, Shneiderman, TODO
- [[digital-music-object]], music as an evolving digital artifact (FAST project output), TODO
- [[professional-practice-overview]], the CM2045 module map (3 pillars, 5 areas), TODO
- [[agile-methodologies]], previewed for the teamwork/project-management topic, TODO
