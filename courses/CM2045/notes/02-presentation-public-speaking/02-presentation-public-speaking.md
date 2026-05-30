# Topic 2: Presentation & Public Speaking

> CM2045 · Topic 2 (Presentation & Public Speaking) · 9 lectures
> Source transcripts: `notes/transcripts/02-presentation-public-speaking/` (local, gitignored)

## TL;DR
Public speaking is a **masterable skill**, even senior academics and industry pros feel nervous; the goal is **managing nervous energy**, not eliminating it. The fundamentals are **voice control, body language, eye contact, and confidence**, delivered through **structured, engaging, audience-tailored content**. The repeated golden rule is **know your audience** and adjust technical depth accordingly (engineers vs non-technical stakeholders). A strong presentation follows a **problem → solution → results** spine with clear transitions, uses **visuals to simplify complexity** (see [[presentation-zen]] for the deep dive), and treats **Q&A as an asset**: questions show engagement and let you reinforce your message. The **elevator pitch** distills all of this into ~30-60 seconds: lead with a hook and benefit, not jargon. Computer scientists must especially **bridge technical and non-technical audiences**, a skill that directly boosts **employability** in interviews and assessment centres. Practice, honesty about what you don't know, and **transferable employability skills** (communication, emotional intelligence, collaboration) are the throughline.

## 1. Why public speaking matters and managing nerves ([[managing-presentation-nerves]])

- Public speaking is **intimidating but learnable** with practice and the right techniques.
- **Everyone feels nervous**, including senior academics and industry experts who appear calm; the skill is turning that nervous energy into something **positive**, not removing it.
- Core fundamentals to master (likely exam fodder):
  - **Voice control**
  - **Body language**
  - **Eye contact**
  - **Confidence / managing nervousness**
- These lectures are deliberately **simple and short**, built on the **CAFE model** (a pedagogical framework that keeps the speaker on point and prevents irrelevant tangents). Simplicity is **by design**: depth comes from activities, readings, discussions, and peer review.
- By topic's end you should be able to **deliver, engage, and persuade** for any audience.

## 2. A worked example: an academic conference talk ([[heuristic-evaluation]])

Lecture 2 is a real recorded conference presentation (Dr Sean McGrath, *"Breaking the Workflow: Design Heuristics to Support the Development of Usable Digital Audio Production Tools"*). It doubles as a **content example** (watch how a real talk is structured) and a **domain case study**. Key content points:

- **Premise:** digital audio workstations (DAWs) are good at **functional tasks** but poor at supporting **dynamic, context-driven, collaborative workflows**.
- **Defining the user first** (via participatory design / three workshops). Three roles:

  | Role | Who | Focus |
  |---|---|---|
  | **Performer** | Musician, vocalist, live coder | Making music, ideation |
  | **Producer** | Mixing/mastering, sound engineer | Processing and digitising sound |
  | **Agency** | Label, management, fans, stakeholders | Communication, scheduling, metadata, driving the process |

- An **independent artist** can occupy all three roles at once; systems handle this "all-in" fuzzy overlap poorly.
- **[[usability-heuristics]]** give a lightweight way to classify issues (control, flow, visibility of system status, metaphor/symbolism, consistency of accelerators/shortcuts). Excess **cognitive load** (relearning controls, hunting for hidden functions) breaks a creative's workflow.
- **Findings:** screens poorly support complex input/output visualisation; systems lack **knowledge representation** (no embedded metadata/collaboration); behaviour and controls are **inconsistent** across tools.
- **Design implication:** design for **humans and context**, not just task sequences; borrow ideas like **version control / content management** from software engineering to capture the why behind decisions.

*(Takeaway for presentation skills: note how the talk opens with motivation, defines terms, walks through method, then findings → implications, a clean narrative arc.)*

## 3. Five tips for technical presentations (likely exam fodder)

The central CS-specific skill: balancing **detail with clarity and engagement** for technical audiences.

| # | Tip | Key actions |
|---|---|---|
| 1 | **Know your audience's technical level** | Adapt depth; engineers get algorithms/architecture, managers get high-level outcomes/impact. **Never assume** shared background; give brief context first so no one is lost and experts can re-engage. |
| 2 | **Use visuals to simplify complexity** | Flowcharts, network diagrams, code snippets. Highlight key points; don't overload. Live demos engage but **always have a backup plan**. |
| 3 | **Structure for clarity and flow** | Start with the **big picture** (what problem, why), then break into digestible sections (**problem → solution → results**). Use explicit **transitions** to reorient the audience. |
| 4 | **Anticipate and address questions** | Predict likely questions; weave answers into the content preemptively. If you don't know, say *"I'll look into that and get back to you"*, never bluff (it kills credibility). |
| 5 | **Use real-world examples and case studies** | Ground theory in practice; **quantify results** (e.g. "reduces processing time by 50%", before/after). Technical audiences love **data** and concrete outcomes. |

## 4. The elevator pitch ([[elevator-pitch]])

*(Lectures 4 & 5 flattened: a "before" and "after" version of the same machine-learning-in-healthcare pitch by "Alex".)* A pitch must convey value in ~30-60 seconds, lead with a hook and benefit, not internal jargon.

| Aspect | Weak pitch (Lecture 4) | Strong pitch (Lecture 5) |
|---|---|---|
| **Opening** | Defines ML/MRI from first principles, dense definitions | *"I'm passionate about how machine learning is transforming healthcare"*, hook first |
| **Jargon** | Overfitting, underfitting, CNNs, hierarchical features | Plain language; jargon dropped or explained |
| **Evidence** | Vague ("could somehow possibly support doctors") | **Concrete stats**: +20% diagnostic accuracy, 50% faster diagnosis, ~£100bn potential savings |
| **Benefit framing** | Buried under technical mechanism | Clear: earlier/more reliable diagnosis, better patient outcomes, lower cost |
| **Tone** | Hedging, uncertain, rambling | Confident, purposeful, audience-centred |

**Lesson:** lead with **why it matters to the listener**, back claims with **numbers**, strip jargon, and project **confidence**. Same content, radically different impact.

## 5. Using visual aids: Presentation Zen ([[presentation-zen]])

Lecture 6 applies Garr Reynolds' **Presentation Zen** philosophy: **simplicity, restraint, naturalness**, visuals **enhance, never replace**, your message. Core principles: one idea per slide, high-quality relevant images, **minimise text** (the [[six-by-six-rule]]: max ~6 words per line, ~6 lines), use **contrast** to highlight, and structure slides as a **story**. Memory retention is **~65% with a relevant visual vs ~10% without** (likely exam fodder). Pitfalls: overloading slides, ignoring **accessibility** (low contrast, tiny text), and reading off the slides. Tools: Canva, Piktochart, Google Slides/PowerPoint, Venngage.

**See the dedicated deep-dive note: [[presentation-zen]]** (`06-presentation-zen.md`) for the full breakdown of principles, visual-aid types, and tools.

## 6. Handling audience questions ([[handling-audience-questions]])

Q&A is an **asset, not a threat**: it clarifies your message, makes the session a **conversation not a monologue**, and showcases expertise (Carmine Gallo, *Talk Like TED*: Q&A is a chance to show you're knowledgeable and adaptable). Seven-stage workflow:

| Stage | Technique |
|---|---|
| **1. Prepare** | Review your deck for gaps/tricky areas; prepare clarifications and **backup slides** (specs, code, metrics); rehearse with peers who probe you (DeWitt, *Illuminate*: preparation builds confidence). |
| **2. Listen actively** | Don't interrupt; **paraphrase the question back** ("If I understand, you're asking…"); **repeat it for the whole room**; praise good questions to encourage more (Julian Treasure: process intent, not just words). |
| **3. Answer well** | Be **concise** and on-topic; **be honest if you don't know** ("great question, I'll follow up"), Socrates: *"I know that I know nothing"*, humility builds trust; **link back to your key message** (Patterson et al., *Crucial Conversations*). |
| **4. Handle tough/hostile questions** | Stay **calm and composed**, don't get defensive; **pause** to gather thoughts; **refocus** off-topic questions ("happy to discuss after"); **acknowledge other perspectives** before responding. |
| **5. Keep the whole audience engaged** | Make eye contact with **everyone**, not just the asker; scan slowly (e.g. trace alphabet shapes / hit all corners); invite broader participation; use questions to **reiterate key takeaways** (Stephen Lucas, *The Art of Public Speaking*). |
| **6. Close cleanly** | Signal the end ("time for one last question"); **summarise key points**. |
| **7. Invite follow-up** | Share contact (email/social/after event), a **networking opportunity**. |

## 7. Presentation skills for recruitment ([[presentation-skills-recruitment]])

Strong presentation skills give a **competitive edge** in interviews and assessment centres (likely exam fodder).

- **Where it shows up:** structuring interview answers; delivering a **short set-piece presentation** followed by follow-up questions; assessment-centre **case studies** and **group tasks**.
- **What recruiters read into it:** professionalism, preparedness, ability to handle real-world situations and communicate with non-technical stakeholders.
- **The CS-specific demand:** make complex information **accessible**, avoid jargon (or spell out acronyms), use analogies and clear data-focused visuals, tie everything to **company/project goals**; the tech sector rewards **innovative/novel** framing.
- **UoL global employability skills** that presenting exercises: **clear communication**, **emotional intelligence** (read your audience), **collaboration** (rehearse with peers/mentors), **complex problem solving**, **adaptability and resilience**.
- **AI as a tool, not a crutch:** use ChatGPT for content ideas / mock Q&A, PowerPoint's **rehearsal coach** for pacing and tone, grammar checkers; but use **human judgement** for audience targeting and keep delivery human and interactive. UoL's specialist career tools may outperform generic LLMs here.
- **Tailor to your career stage:**

  | Stage | Focus |
  |---|---|
  | **Career starter** | Build confidence; learn structure basics; hit the time limit; answer the actual task |
  | **Career developer** | Refine delivery; align message with growing expertise; shift to a strategic view |
  | **Career changer** | Highlight **transferable skills**; link past experience to the new role |

- Universal advice: **practice, practice, practice**, especially with any **technology** you'll use live; non-verbal cues (eye contact, posture, gestures); design, rehearse, self-reflect.

## 8. Topic summary

Recap of the whole topic: master the **fundamentals** (voice, body language, confidence, controlling nerves); build **structured, engaging, audience-tailored** content; **evaluate and improve** via examples, reflection, and quizzes. The payoff is **career-critical**: confident presenting (pitching ideas, presenting projects, answering tough interview questions) makes you **more employable** and helps build your **professional brand**. Mastering public speaking is about making an **impression**, not just delivering slides.

## Related concepts
- [[managing-presentation-nerves]], turning nervous energy positive, TODO
- [[heuristic-evaluation]], the conference-talk case study (DAW usability), TODO
- [[usability-heuristics]], control/flow/visibility/consistency factors, TODO
- [[elevator-pitch]], the ~30-60s value pitch (weak vs strong), TODO
- [[presentation-zen]], visual-aids philosophy (deep-dive note exists)
- [[six-by-six-rule]], slide text-density rule, TODO
- [[handling-audience-questions]], the 7-stage Q&A workflow, TODO
- [[presentation-skills-recruitment]], interviews and assessment centres, TODO
- [[visual-memory-retention]], the 65/10 retention stat, TODO
- [[uol-employability-skills]], communication, EI, collaboration, problem solving, resilience, TODO
