# Topic 8: Teamwork & Collaboration

> CM2045 · Topic 8 (Teamwork & Collaboration) · 5 lectures
> Source transcripts: `notes/transcripts/08-teamwork-collaboration/` (local, gitignored)

## TL;DR
In tech the **solo programmer is a myth**: software is too **complex**, needs **diverse skills** (programmers, designers, testers, PMs), and **creativity comes from shared perspectives**, so **teamwork is essential, not nice-to-have**. Effective collaboration rests on **clear communication**, **defined roles**, a **shared goal/vision**, a **respectful inclusive environment**, and **agile methods** (Scrum, Kanban, iterative feedback). The toolchain is structured: **version control** (Git, GitHub/GitLab/Bitbucket) as the unsung hero, **project management/agile boards** (Jira, Trello, Asana), **communication** (Slack, Teams, Zoom), **docs/knowledge bases** (Notion, Coda, wikis, SharePoint), **visual/brainstorming** (Miro, Mural, UML), **design** (Figma, Adobe XD), **code review** (Upsource, Crucible), and **CI/CD** (Jenkins, GitLab CI). Conflict is **inevitable and not inherently bad**: the **Thomas-Kilmann Instrument (TKI)** maps five styles (**competing, collaborating, compromising, avoiding, accommodating**) along **assertiveness** vs **cooperativeness**, each fit for different situations. The **employer-voice** lecture (TCS) stresses **playing to strengths**, **shared accountability**, **not micromanaging** (trust + autonomy), conflict resolution via **"it's not personal" + one-to-ones + escalation**, "**respect trumps harmony**", **prioritisation frameworks** to absorb pressure, **setting code-review expectations up front**, and **documentation** as a baseline for the next person.

## 1. Why teamwork matters in computing ([[teamwork-in-computing]])

Solo coding does not scale. The four drivers (likely exam fodder):

| Driver | Why it forces teamwork |
|---|---|
| **Complexity** | OSes, social platforms, self-driving cars: no one person can build them |
| **Diverse skills** | Programmers, designers, testers, project managers each bring expertise |
| **Creativity & problem-solving** | Different perspectives spark innovation; ideas flourish through collaboration |
| **Learning & growth** | You learn from others, gain insight, improve, become a better computer scientist |

### Inspiring examples (good for illustrating answers)
- **Apollo 11:** a massive team of engineers, mathematicians, programmers under intense deadline pressure with a proactive can-do attitude and shared belief.
- **Linux kernel:** a global community of online volunteers; started by one person, grew into distributed open-source teamwork.
- **World Wide Web:** Tim Berners-Lee did not build it alone; researchers, engineers and organisations built on existing standards with small incremental improvements.
- **COVID-19 tracking apps:** developers, medics and designers worked rapidly with agile methods; vaccines built across industry and public sector.
- **Mars rover software:** NASA/ESA teams use rigorous testing and collaboration; diverse hiring and cross-domain expertise underpin large research efforts.

## 2. Principles of effective collaboration ([[effective-collaboration]])

| Principle | What it means in practice |
|---|---|
| **Clear communication** | Slack, meaningful commit messages (`-m` flags), PM software, regular meetings; **stand-ups** keep everyone informed and accountable (an agile technique) |
| **Defined roles & responsibilities** | Who does what; avoids confusion and duplicated effort. A **Kanban board** (e.g. Trello) visualises who works on what |
| **Shared goals & vision** | Everyone understands objectives and works toward the same outcomes |
| **Respectful, inclusive environment** | Review everyone's contributions, listen actively, stay open to other perspectives |
| **Agile methodologies** | Iterative development, frequent feedback, adapt to change; **Scrum** and **Kanban** are the friends, **design thinking** can embed the process |

- **Code is a team sport:** without the right tools, teamwork becomes a tangled mess of conflicting changes, miscommunication and missed deadlines. The right tools **streamline workflows** and **automate tasks**.
- **Sprints** typically run ~**two weeks** delivering a handful of high-priority features (lecturer aims for ~**3–5**), variable by scope.
- **User-centred design:** show users designs and gather feedback each iteration; even **paper prototyping** helps weed out bad ideas fast.

## 3. Collaboration tools by category ([[collaboration-tools]])

| Category | Tools | Use case |
|---|---|---|
| **Version control** (the unsung hero) | **Git** (champion), GitHub, GitLab, Bitbucket | Many devs on one codebase; track + merge changes; **branching = parallel universes** to experiment without breaking `main`. Older CVS/SVN/Subversion were limited; Git won on power + simple syntax |
| **Project management / agile boards** | **Jira, Trello, Asana** | Visualise progress, track + prioritise tasks; Kanban moves work from backlog to done; sprint planning + retrospectives |
| **Communication** | **Slack, Microsoft Teams** | Quick chat, file sharing, team community; empathetic voices help move past blockers |
| **Video conferencing** | **Zoom** | Real-time face-to-face discussion, webinars |
| **Documentation / knowledge base** | **Notion, Coda, wikis, SharePoint** | Living, searchable hub; document decisions + design rationale; unit-test frameworks also document features |
| **Visual / brainstorming** | **Miro, Mural** (infinite whiteboards); **UML** | Mind-maps, sticky notes, user flows, architecture; **UML class/activity/sequence diagrams** and use cases; powerful for **distributed teams** |
| **Design / prototyping** | **Figma, Adobe XD** | Collaborate on UI/UX, gather feedback, interactive prototypes |
| **Code review** | **Upsource, Crucible** | Side-by-side diffs, threaded discussion, Git integration; catch bugs early, share knowledge, ensure consistency |
| **Testing / CI/CD** | **Jenkins, GitLab CI** | Automate testing + deployment for quality and faster releases; run unit tests automatically against changes |
| **IDE collaboration** | IDEs (e.g. VS Code extensions) | Shared coding sessions, real-time review, pair programming |

- **Choosing tools (likely exam fodder):** collaboration is **not one-size-fits-all**; tailor to **team size, project type, working style**. Information overload is a real risk.
- **Code review as culture:** an opportunity for **mentorship and skill development**; explaining your code teaches you too. Reviews **break down silos** so information flows across departments.

## 4. Managing team conflict: the TKI ([[conflict-management]])

Conflict is **part of the daily grind**, not a TV drama: tabs vs spaces, naming conventions, architecture, "whose bug is it", front-end vs back-end, UX vs technical feasibility, and **agile/story-point** disputes (guessing without **data-driven metrics**). The goal is to **master conflict, not avoid it**.

The **Thomas-Kilmann Conflict Mode Instrument (TKI)** maps five styles on two axes: **assertiveness** (pursuing your own concerns) vs **cooperativeness** (pursuing others'). (likely exam fodder)

| Style ("code persona") | Assertive | Cooperative | When useful | Drawback |
|---|---|---|---|---|
| **Competing** (code crusader) | High | Low | Critical bug quick-fix, urgent security vuln, technical impasse; small orgs avoiding bureaucracy | Alienates teammates, stifles alternatives, toxic if overused |
| **Collaborating** (code diplomat) | High | High | Designing complex systems, refactoring legacy code, brainstorming | Time-consuming; bad when a quick decision is needed |
| **Compromising** (code negotiator) | Moderate | Moderate | Resolving merge conflicts, integrating modules, time constraints | Suboptimal solutions; some left partially dissatisfied |
| **Avoiding** (code ostrich) | Low | Low | Minor or personality-driven conflict, emotions running high; suits independent devs | Problems fester, hurts cohesion, blocks valuable feedback |
| **Accommodating** (code peacemaker) | Low | High | Preserving team harmony, learning from a senior, issue matters little to you | Breeds resentment if overused, suppresses useful perspectives |

- **No single "right" style:** **mix and match strategically** to keep the team productive and feeling good about the work.

## 5. Employer voice: TCS practitioners ([[employer-voice-teamwork]])

Interviews with **Ritwik Shyam** (data scientist, TCS Innovation, UK & Ireland) and **Tanvi** (lead, TCS Early Careers, UK & Ireland). Practical takeaways:

### What effective teamwork is
- **Play to each other's strengths** on a **common/shared objective**; getting along is the non-negotiable baseline, but the core is **shared accountability**.
- Know teammates' **strengths and weaknesses** so support is in place when someone works outside their best area.
- In tech you mix **technical, domain and functional experts**: treat each as an **equal expert**; the end goal is **project/customer success**, not individual glory.

### Management behaviours that help
- **Do not micromanage.** Good managers give **high-level guidance and the roadmap**, then leave task-level decisions to the team. This rests on **trust + autonomy** ("facilitator / enabler"). (likely exam fodder)
- Culture flows from **values**: TCS cites **excellence** and **respect for individuals**; hire for **value alignment**, then bridge gaps via training or team moves ("unlearn and relearn").

### How an individual contributes
- **Be proactive, drive change** rather than waiting top-down. For a new tool: **start using it yourself, show value, lead by example** ("**show, don't tell**", "practise what we preach").

### Conflict resolution (employer view)
- **Mindset: "it's not personal."** Give the **benefit of the doubt**; setbacks rarely stem from ulterior motives.
- **Start with a private one-to-one**, do not broadcast or make it a group setting; **bring focus back to the shared objective**.
- **Communication, communication, communication** is the key (Tanvi). If unresolved, **escalate to manager / HR**, severity-dependent, always in a closed setting.
- **"Respect trumps harmony"** (book Tanvi's manager recommended): respect the person and their thinking, but **disagree when it serves the greater good**; short-term friction, long-term appreciation.
- Different skill sets producing **different approaches is a strength to leverage**, not a threat.

### Managing pressure (feature creep, big backlogs, unrealistic goals)
- **Ideate unconstrained first**, then layer on constraints/regulatory criteria to **filter out infeasible ideas**: not every point needs debate.
- **Prioritisation framework** (set by the manager) gives **common minimum alignment**: teams may differ on approach but agree on priority. (likely exam fodder)

### Code review without crushing morale
- **Set guidelines, testing principles and quality expectations up front**, not sequentially after the code is written, so authors do not feel **unfairly targeted**.
- Provide **exemplars/benchmarks** and **documentation** so the next person starts from a higher baseline instead of meeting a critique cold. Client-facing/client-data work faces **~10x more scrutiny**.

### Inclusion and underperformance
- **Surface quiet voices:** ask for specific feedback, hold one-to-ones, run **anonymous surveys**, **give people responsibility** to draw them out; reiterate **project success over individual glory**.
- **As teams grow,** challenges shift (e.g. **cultural**): return to **shared values**, anticipate and train where possible, learn the rest on the job.
- **Underperformance:** identify **early**, validate with another senior, then have a **direct conversation** to find the cause (lack of support, skill, or equipment). Try training, extra help, or a **team move** for skill mismatch. If none works, it is an **attitude/behavioural** issue, a different problem entirely.

### What makes a good team worker (advice for students)
- Someone who **lets you be in your element**: you perform your best, learn from them, and work feels **effortless/seamless**. A good dynamic **listens to everyone**, not just the loudest voice, and stays **objective**.
- **Cultivate it:** **empathy**, and above all **understand your team** (strengths, weaknesses, likely conflict points). It is a **two-way street**, so be proactive.
- **Students:** put your thoughts forward, **do not be afraid of being wrong** (have a counterpoint, or the humility to accept a better idea), and **keep the team goal in mind**: individual goals follow.

## Related concepts
- [[teamwork-in-computing]], why solo coding does not scale: complexity, skills, creativity, growth
- [[effective-collaboration]], communication, roles, shared vision, inclusion, agile
- [[collaboration-tools]], the categorised toolchain (VCS, PM, comms, docs, design, review, CI/CD)
- [[conflict-management]], the Thomas-Kilmann five-style model
- [[thomas-kilmann-instrument]], assertiveness vs cooperativeness grid, TODO
- [[employer-voice-teamwork]], TCS practitioner takeaways
- [[agile-methodologies]], Scrum, Kanban, sprints, retrospectives, TODO
- [[version-control]], Git, branching/merging, GitHub/GitLab/Bitbucket, TODO
- [[code-review]], mentorship, knowledge-sharing, setting expectations up front, TODO
- [[user-centred-design]], iterative feedback, prototyping, TODO
- [[uml]], class/activity/sequence diagrams and use cases for shared understanding, TODO
- [[psychological-safety]], "not personal", respect trumps harmony, safe critique, TODO
