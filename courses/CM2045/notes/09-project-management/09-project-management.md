# Topic 9: Project Management

> CM2045 · Topic 9 (Project Management) · 6 lectures
> Source transcripts: `notes/transcripts/09-project-management/` (local, gitignored)

## TL;DR
The topic traces the shift from **waterfall** (rigid, plan-everything-upfront, costly rework) to **Agile**, a *mindset, not a rule set*, codified in the **2001 Agile Manifesto** (17 authors, four values: individuals/interactions over processes/tools, working software over documentation, customer collaboration over contract negotiation, adaptability over following a plan). Two frameworks dominate: **Scrum** (iterative/incremental **sprints** of 2–4 weeks, with three **roles**, three **artifacts**, and five **events**) and **Kanban** (a **visual workflow** board born from Toyota's **lean / just-in-time** manufacturing, centred on **limiting work in progress** and optimising **flow**). Real adoptions are mixed: **Spotify** (squads/tribes/chapters/guilds), **Microsoft** (gradual, hybrid), and **Etsy** (continuous deployment) show that **context and culture decide success**, while the **Agile backlash** (Agile-fall, cargo-cult Agile) warns against following ceremonies without the values. The lecturer flags **story points** as a *false metric* (estimation is guessing). Topic closes on **timeless techniques** (Kanban, sprint planning templates, automation, risk management, communication/meeting hygiene) and **UoL careers micro-modules** for building PM skills.

## 1. Waterfall and the rise of Agile ([[agile-manifesto]])

- **Waterfall** = "the old way": design every detail, then foundation, then walls, **no changes allowed**. Like building a house to a fixed blueprint.
  - **Rigid and inflexible.** Good for **predictable** projects, but software rarely is. Changing requirements means **costly rework**.
  - The **original waterfall paper actually warned against its use** (likely exam fodder): it can be rigid, inefficient, and ignore user-centred design.
  - Assuming scope/features stay fixed for a decade "almost seems laughable" given how fast the world changes.
- **Why Agile emerged (late '90s):** the internet/web boomed, compute power rose, and the market demanded faster, better software.
- **2001:** 17 software gurus met (they did *not* all agree) and produced the **Agile Manifesto**, four core values (likely exam fodder):

| Value | ...over |
|---|---|
| **Individuals and interactions** | processes and tools |
| **Working software** | comprehensive documentation |
| **Customer collaboration** | contract negotiation |
| **Adaptability / responding to change** | following a plan |

- **Agile is principles, not rules; a mindset, not rigid procedures.** Lecturer's view: it maps closely onto **usability principles and user-centred design** from 1990s CHI research.
- **Agile flavours mentioned:** **Scrum** (sprints, stand-ups, retrospectives), **Kanban** (visual workflow, limit WIP, optimise flow), and **Extreme Programming (XP)** (technical practices: **pair programming**, **test-driven development**, **continuous integration**). TDD pairs well with a Kanban board (features "appear" as unit tests pass).
- **Payoff:** faster releases, happier customers, more adaptable teams ("they call them sprints for a reason").

## 2. The Agile backlash ([[agile-backlash]])

Many organisations adopted Agile **in name only** (likely exam fodder):
- **Agile-fall:** calling it Agile while keeping rigid waterfall structures. Does not produce results.
- **Cargo-cult Agile:** blindly following **ceremonies and rituals** without understanding the **underlying principles**.
- Even the **Manifesto authors criticise** how it is implemented, stressing focus on **values, not just practices**.
- Lecturer's caution on **story points**: a **false metric**, "it's guessing", and empirical evidence says developers (even experienced ones) are poor at predicting how long work takes. **Focus on outcomes, not processes.**
- **Future of Agile:** adapt, experiment, embrace **continuous improvement**, stay true to core values; check that a trend (tool or stack) actually fits *your* problem, company, and culture.

## 3. Scrum fundamentals ([[scrum]])

**Scrum** = an Agile framework that is **iterative and incremental**, breaking projects into short cycles called **sprints** (usually **2–4 weeks**). Teams are **self-organising**, with **continuous feedback** via reviews and retrospectives. (All of section 3 is likely heavily tested.)

### Roles (likely exam fodder)
| Role | Responsibility |
|---|---|
| **Product Owner** | Represents the customer, defines the **product vision**, **prioritises the backlog** (the features to build) |
| **Scrum Master** | Facilitates the process, **removes impediments**, ensures adherence to Scrum principles. **Process-focused, not product-focused** |
| **Development Team** | The **self-organising** group that actually builds the product |

### Artifacts (likely exam fodder)
| Artifact | What it is |
|---|---|
| **Product backlog** | Prioritised list of features/requirements. Priority emerges from **most value to users** + **easiest to build** (both = highest priority) |
| **Sprint backlog** | The subset of product backlog the team **commits** to in a sprint. A collection of features = a **Minimum Viable Product (MVP)** |
| **Increment** | The **working software** produced at the end of each sprint (e.g. version 0.0.0.1) |

### Events (likely exam fodder)
| Event | Purpose |
|---|---|
| **Sprint planning** | Team plans the upcoming sprint's work (estimates improve with experience) |
| **Daily scrum** | Short daily sync on progress, typically a quick **stand-up** then back to work |
| **Sprint review** | Demonstrate the increment to **stakeholders**, gather feedback. A **must** for buy-in and to verify/validate against expectations |
| **Sprint retrospective** | Team reflects on the sprint and identifies improvements (critical evaluation drives improvement) |

- **Why Scrum works:** **flexibility** (adapts to changing priorities), **collaboration**, **transparency** (visible progress/challenges), **continuous improvement**.
- **Applies beyond software:** mobile apps, websites, even marketing campaigns and research projects, anything needing flexibility and collaboration.
- Lecturer recruits **outside their own expertise** so team skills complement each other and reduce knowledge gaps.

## 4. Kanban basics ([[kanban]])

**Kanban** = a **visual approach to workflow management**. Roots are in **manufacturing**: **Toyota's production system, 1940s**, inspired by how supermarkets restock shelves (**lean manufacturing**). (All of section 4 is likely heavily tested.)

- **Just-in-time inventory:** only replenish items when needed, minimise waste, maximise efficiency.

### Kanban principles (likely exam fodder)
| Principle | Meaning |
|---|---|
| **Visualise the workflow** | Make all work items and their status visible: who is working on what, when, and what stage it is at |
| **Limit work in progress (WIP)** | Finish tasks before starting new ones; reduces multitasking, improves flow |
| **Manage flow** | Continuously monitor/improve flow, identify and clear **blockages** (a blockage is a lesson) |
| **Make process policies explicit** | Clearly define how work moves through the system (generally left to right) |
| **Improve collaboratively** | Continuous improvement via feedback and experimentation |

### The Kanban board
- **Columns** = stages: **To Do, In Progress, Testing, Done** (each phase can have its own testing/QA gate before work moves on).
- **Cards** = work items, each holding the task, its **assignee**, and **status**.
- **Swim lanes** = categorise cards by project, team, or priority (lecturer sorts by **priority first**, then assigns to specialised teams/individuals around their workload).

- **Uses in CS:** software dev (user stories, bug fixes, features), IT support (incident tickets, service requests), research (tasks, experiments, publication milestones).
- **Kanban complements Scrum**, adding a **visual layer** for managing workflow.
- **Benefits:** improved visibility, reduced waste, increased flow (clear bottlenecks), enhanced collaboration, continuous improvement. "Not just sticking notes on a board", it is a culture of continuous improvement.

### Scrum vs Kanban (quick contrast)
| | **Scrum** | **Kanban** |
|---|---|---|
| **Cadence** | Fixed-length **sprints** (2–4 weeks) | **Continuous flow**, no fixed iterations |
| **Origin** | Software/Agile | Toyota / **lean manufacturing**, 1940s |
| **Defined roles** | Product Owner, Scrum Master, Dev Team | No prescribed roles |
| **Core control** | Sprint commitment + ceremonies | **Limit WIP**, optimise flow |
| **Artifacts** | Product/sprint backlog, increment | Board (columns, cards, swim lanes) |
| **Relationship** | A full framework | **Complements** Scrum (visual layer) |

## 5. Agile case studies ([[agile-project-management]])

| Company | Era | Approach | Went well | Did not work | Lesson |
|---|---|---|---|---|---|
| **Spotify** | ~2012 | "**Scaling Agile at Spotify**" model: **squads** (small cross-functional autonomous teams), **tribes** (collections of related squads + tribe lead), **chapters** (same-skill groups across squads, e.g. devs/designers), **guilds** (lightweight communities of interest). Frequent releases + **A/B testing** | More autonomy/motivation, faster innovation, better product quality | Maintaining **alignment** as it grew, **dependency** bottlenecks between squads, hard to **replicate** elsewhere | **Context matters**; **autonomy requires alignment** (clear goals, shared values); **culture is key** |
| **Microsoft** | early 2000s on | **Gradual** adoption: pilot projects, heavy **training and coaching**, tooling (**Visual Studio Team Services → Azure DevOps**), **hybrid** Agile + waterfall | Better quality, higher morale, faster time to market | **Resistance to change**, deep waterfall habits, scaling across a massive org | **Change takes time**; **training is essential**; **adaptation is key** (Agile does not fit everywhere) |
| **Etsy** | ~2008–2009 | **Continuous deployment**: automated build/test/deploy (many deploys/day), **small frequent changes**, comprehensive **automated testing**, **DevOps culture** | Rapid iteration/feedback, higher developer productivity, improved site stability | Keeping code quality at high deploy frequency, **managing risk** (needed **rollback**/mitigation), cross-team coordination | **Automation is key**; **culture of trust**; **continuous improvement** |

- **Recurring themes (likely exam fodder):** data-driven decision-making, automation freeing developers from monotonous tasks, robust testing + version control for safe rapid change.
- **Closing point:** Agile is **no longer a competitive advantage but a prerequisite** for success in dynamic, fast-paced environments.

## 6. Timeless PM techniques (tool-agnostic) ([[agile-techniques]])

**Tools are transient; techniques are timeless.** Today's popular PM app may be obsolete tomorrow, so master the underlying techniques that work on a whiteboard or in sophisticated software.

- **Kanban in action (analogue):** a whiteboard + sticky notes; map stages (**To Do / In Progress / Done**), limit WIP by **physically limiting space** per stage.
- **Sprint planning templates** structure the sprint:
  - **Sprint goal** (one concise statement of the aim)
  - **Sprint backlog** (prioritised tasks from the product backlog)
  - **Task breakdown** (decompose user stories into smaller tasks)
  - **Effort estimation** (story points or time estimates, note the lecturer's earlier scepticism on story points)
- **Automation (e.g. Selenium):** primarily web-test automation, but can also generate reports/**burn-down charts**, auto-update task status from commits/test results, and send notifications. Frees time for strategic work.
- **Risk management** (even small projects carry risk):
  1. **Risk identification** (brainstorm and document)
  2. **Risk assessment** (likelihood + impact, low→high, e.g. in a simple spreadsheet)
  3. **Risk mitigation** (reduce likelihood/impact)
  4. **Risk monitoring** (track and adjust through the lifecycle)
- **Communication, match message to medium:**

| Medium | Best for |
|---|---|
| **Instant messaging** (Slack, MS Teams) | Quick questions, informal updates, real-time collaboration |
| **Video conferencing** (Zoom) | Richer/complex discussion, brainstorming, team building |
| **Project wikis** (Confluence, Notion) | Central documentation, knowledge sharing, updates |
| **Face-to-face meetings** | Critical decisions, relationship building (Agile advocates this; lecturer is sceptical, noting students chose remote study) |

- **Effective meetings:** clear objectives, **prepared/circulated agendas**, **time-boxing** per item, **active participation**, **concise minutes** (good minutes mean no need to repeat things).

## 7. Building PM skills for your career ([[career-pm-skills]])

- **UoL Career Service** offers **careers/employability micro-modules** on the VLE; each gives a **certificate of completion recognised on your degree transcript**.
- Three micro-modules (at time of recording): **Global Employability Skills**, **Professional Impact Profile and Success**, **Career Planning**.
- **Professional Impact Profile and Success** has the most PM content; four strands: the **persuasive professional** (negotiating), the **strategic professional** (time management), the **entrepreneurial professional** (a dedicated **project management** section on the **three phases of the project lifecycle**), the **market-aware professional**.
- **Practise PM outside work:** at home (childcare, home improvement, gardening), in the community (volunteering on projects), in your studies (apply PM to study habits, and apply studies to work tasks).
- Provides worked examples of how to **evidence PM skills** in a CV, application, or interview (e.g. distance-learning study demonstrating time management, prioritisation, flexibility, and liaising with a line manager to align study and work).

## Related concepts
- [[agile-manifesto]], 2001, four values; mindset over rules
- [[agile-backlash]], Agile-fall and cargo-cult Agile; values over ceremonies
- [[scrum]], roles/artifacts/events, sprints
- [[kanban]], visual workflow, limit WIP, lean/just-in-time roots
- [[agile-project-management]], Spotify / Microsoft / Etsy case studies
- [[agile-techniques]], tool-agnostic PM techniques (sprint planning, risk, comms)
- [[career-pm-skills]], UoL careers micro-modules
- [[waterfall-model]], the rigid predecessor to Agile, TODO
- [[extreme-programming]], pair programming, TDD, CI, TODO
- [[test-driven-development]], TODO
- [[continuous-deployment]], Etsy's many-deploys-a-day approach, TODO
- [[user-centred-design]], the lecturer ties Agile back to 1990s CHI/UCD, TODO
- [[minimum-viable-product]], a collection of features demoed early, TODO
- [[story-points]], the contested estimation metric, TODO
- [[burn-down-chart]], progress metric automatable via Selenium, TODO
