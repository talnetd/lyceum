# Topic 4: Inclusive Computing

> CM2045 · Topic 4 (Inclusive Computing) · 9 lectures
> Source transcripts: `notes/transcripts/04-inclusive-computing/` (local, gitignored)

## TL;DR
**Inclusive computing** designs technology usable by the widest range of people, regardless of physical, cognitive, sensory ability, language, socioeconomic status, or culture. The stakes: **~15% of the global population (≈1 billion people)** lives with some disability, so non-inclusive tech excludes them. Two threads run through the topic. First, **ethical impacts**: privacy (Cambridge Analytica, Snowden), **algorithmic bias** (Amazon's sexist recruiter, facial recognition's **34.7%** error rate for dark-skinned women, Robert Williams' wrongful arrest), automation/job displacement, the self-driving **trolley problem**, and the **digital divide** (exposed by COVID). Second, **accessibility**: **universal design** (the "curb-cut effect", design for one extends to many), with case studies from **Microsoft** (Immersive Reader, Xbox Adaptive Controller), **Google** (Project Euphonia), and the **BBC** (subtitles, audio description, accessible iPlayer to **WCAG 2.1**). Law bites: the **ADA** (Domino's lost in the US Supreme Court), the EU **Web Accessibility Directive**, the **UK Equality Act 2010**, the EU **AI Act**, and **GDPR**. Practitioner toolkit: **inclusive design thinking**, diverse teams, accessibility-first dev (**WCAG**, alt text, **ARIA**, keyboard nav), bias mitigation (**IBM AI Fairness 360**), diverse user testing, and **ethical impact assessments (EIAs)**.

## 1. What is inclusive computing ([[inclusive-computing]])

- **Definition:** designing technology usable by the widest range of people regardless of **ability or circumstance**, accounting for physical, cognitive, and sensory abilities plus language barriers, socioeconomic factors, and cultural diversity.
- Not just *available* to everyone, but **usable and enjoyable** for everyone.
- **The number to know (likely exam fodder):** ~**15% of the global population**, roughly **1 billion people**, live with some form of disability. Non-inclusive tech excludes them.
- **Inclusivity drives innovation:** designing for everyone pushes the boundaries of what's possible.

### Core inclusive-design principles
| Principle | Meaning | Example |
|---|---|---|
| **Flexibility in use** | Offer multiple ways to interact | Websites with both text and voice controls |
| **Simple and intuitive** | Easy to understand for a first-time user | Low-learning-curve interfaces |
| **Perceptible information** | Provide info in multiple formats | Captions on video (also helps people in noisy environments) |

### Flagship examples
- **Microsoft Xbox Adaptive Controller** (2018): large buttons + ports for gamers with limited mobility. See §4.
- **Google Project Euphonia:** AI trained on **non-standard speech patterns** to help people with speech impairments use voice recognition.

## 2. Ethical impacts of technology ([[ethical-impacts-of-technology]])

Tech has positive effects (medicine, communication, education) and negative ones (privacy breaches, automation anxiety, digital divide). The key framing: *just because we **can** build it doesn't mean we **should**.* The lecturer deliberately blurs topic boundaries so concepts recur at granular and abstract levels.

### The major ethical impact areas (likely exam fodder)
| Area | Key facts / cases | The ethical question |
|---|---|---|
| **Privacy** | **79% of Americans** worried about company data use (Pew); **Snowden / NSA** surveillance | How much privacy will we trade for security/convenience? |
| **Privacy (case)** | **Facebook / Cambridge Analytica** (2018): harvested millions of users' data without consent for 2016 US election ads → outrage, fines, **GDPR**. "We're not Facebook's customers, we're its product." | Balance innovation vs consent + transparency |
| **Bias in AI** | **Amazon** recruiting tool penalised resumes with "women" / women's colleges (trained on 10 yrs of mostly-male CVs) | How do we make AI fair + transparent in high-stakes use? |
| **Bias (facial recognition)** | MIT: **34.7%** error for dark-skinned women vs **<1%** for light-skinned men; **Robert Williams** wrongfully arrested in Detroit (2020) | Discrimination + accountability |
| **Automation / jobs** | Oxford: up to **47% of US jobs** automatable in two decades; affects white-collar too (accountants, radiologists) | Who benefits, tech firms or displaced workers? |
| **Self-driving cars** | The **trolley problem** in real life (hit pedestrian vs risk passenger); Tesla, Waymo grapple with it | Who decides the ethical framework? Premium "save-me" option = unfair |
| **Digital divide** | Only **60% of the world** has internet; COVID exposed it: **16M US students** lacked remote-learning tools | Is a tech-driven world ethical if billions are left behind? |

### Mitigation strategies
- **Ethical design principles:** bake transparency, fairness, privacy in from the start.
- **Diversity in tech teams:** reduces bias in what gets built.
- **Stronger regulation + accountability:** e.g. GDPR holds firms accountable for data + AI use.
- **Public education:** so users make informed choices about products and the privacy they trade.

## 3. Accessibility in software design ([[accessibility]])

*(Software-design lectures 1, 2 & 3 flattened: principles + Microsoft, Xbox, and BBC case studies.)*

- **Accessibility** = designing tech usable by people of **all abilities**, including physical, sensory, cognitive, and learning disabilities. "A human feature, not just a technical feature."
- **WHO:** **1 billion people (≈15%)** live with a disability, so inaccessible software excludes a huge potential user base.
- **Tim Berners-Lee:** *"The power of the web is in its universality. Access by everyone regardless of disability is an essential aspect."*

### Universal design and the curb-cut effect (likely exam fodder)
- **Universal design:** products designed to be accessible to the **widest possible range** of people; designing for all makes the product better for everyone (win-win).
- **Dropped curb / curb-cut:** built for wheelchair users, ended up helping parents with strollers, cyclists, delivery people. Software parallel: **voice recognition** and **text-to-speech** began as accessibility features, now used by millions for convenience.
- Microsoft's **Immersive Reader** (built for dyslexia) improved reading comprehension for *all* users (British Dyslexia Association study), the same effect.

### Key accessibility features to integrate
| Feature | Who it serves | Implementation notes |
|---|---|---|
| **Screen reader support** | Visual impairments | Compatible with **JAWS / NVDA**; provide **alt text**, structured text |
| **Keyboard navigation** | Motor impairments | Every interactive element reachable via **Tab**; no mouse required |
| **Colour contrast + text size** | Low vision, colour blindness | High contrast, adjustable fonts; **WebAIM contrast checker** |
| **Captions + transcripts** | Hearing impairments (and noisy environments) | **80%** finish a video when captions are present (Facebook study) |

### Case study: Microsoft accessibility
- A decade of accessibility-first design across Windows, Office, Xbox. Mission: *"empower every person and every organization on the planet to achieve more"*, including the **1 billion** with disabilities.
- **Immersive Reader** (2019, Word & Outlook): chunk text, change font/spacing, highlight syllables, AI **read-aloud**.

### Case study: Xbox Adaptive Controller ([[xbox-adaptive-controller]])
- Launched **2018**, built with the **AbleGamers** charity and **SpecialEffect**, for gamers with limited mobility. **46M US gamers have disabilities** (ESA).
- **Design = modularity + customisation:**

| Feature | Detail |
|---|---|
| **Ports** | **19 × 3.5mm jacks + USB** for foot pedals, chin joysticks, oversized buttons |
| **Large buttons** | Two programmable face buttons, remappable to any in-game function |
| **Mounting** | Works with wheelchairs, stands, mounts |
| **Software** | **Xbox Accessories App** remaps controls, adjusts sensitivity |

- **Ethical wrinkle (potential misuse):** able-bodied competitive players could remap to streamline combos / rapid-fire (e.g. foot pedals for sprinting), an **unfair advantage**. Mitigations: **fair-play policies**, **monitoring competitive play** (anti-cheat-style flagging of unusual setups), and **educating** the community on its true purpose.
- **Ripple effect:** Sony added custom button mapping/modularity to PlayStation; **Logitech** launched adaptive accessories compatible with it.

### Case study: BBC accessibility strategy
- Public service broadcaster; **>11 million UK people** live with a disability (ONS). Goal: an inclusive society, not just legal box-ticking.
- Components: **subtitles/closed captioning** (nearly all programmes, incl. live), **audio description** (committed to **≥20%** of content; e.g. Doctor Who, Peaky Blinders), **British Sign Language** interpretation, **accessible iPlayer**.
- **Accessible iPlayer:** keyboard nav, voiceover support, customisable subtitles (text size, contrast); built with **GDS (Government Digital Services)** to meet and exceed **WCAG 2.1** (likely exam fodder).
- **AI real-time captioning:** Ofcom found BBC live subtitling **>98% accurate**, far above industry standard.
- R&D frontier: **haptic feedback / wearables** (feel the crowd roar via a wristband), voice-controlled interfaces, AR overlays of sign-language interpreters on live events.

### Accessibility law (likely exam fodder)
| Law / regime | Jurisdiction | What it requires |
|---|---|---|
| **Americans with Disabilities Act (ADA)** | US | Businesses/public services make websites + digital products accessible |
| **Web Accessibility Directive** | EU | Public-sector websites/apps meet accessibility standards; fines for non-compliance |
| **Equality Act 2010** | UK | Public institutions make **reasonable adjustments** so disabled people can access services |

- **Domino's Pizza case (2019):** blind user **Guillermo Robles** couldn't order via screen reader. Domino's argued the **ADA (1990)** predated the internet; the **US Supreme Court** sided with Robles. Lesson: **digital accessibility is no longer optional**, treat it like a physical wheelchair ramp.
- **Business benefits beyond compliance:** higher engagement, customer loyalty, and innovation (the curb-cut effect again).

## 4. Implementing inclusive practices ([[inclusive-practices]])

Why it pays: **McKinsey**, companies with higher diversity are **35% more likely** to beat their industry's median financial returns. Tim Cook: *"the most diverse group will produce the best product."*

### Practitioner strategies (likely exam fodder)
| Strategy | What it means | Tool / example |
|---|---|---|
| **Inclusive design thinking** | Consider diverse needs from the very start; ask *"who is excluded by this design?"* | **Microsoft Inclusive Design Toolkit**; principle **"design for one, extend to many"** |
| **Diverse development teams** | More perspectives catch problems early | Google's diverse hiring → Maps wheelchair routes, voice nav |
| **Accessibility first** | Not an afterthought; build it into core functionality | **WCAG**: high contrast, keyboard nav, screen-reader compat (e.g. Slack) |
| **Bias detection + mitigation** | Test models against fairness metrics | **IBM AI Fairness 360** |
| **Diverse user testing** | Test with disabled users, multiple languages, varied literacy | Apple tests VoiceOver / Magnifier with visually impaired users |
| **Writing inclusive code** | Adaptable to languages, screen sizes, assistive tech | Descriptive **alt text**, **ARIA roles**, clear/neutral variable names, labelled HTML |
| **Ongoing training** | Accessibility is not set-and-forget | Adobe internal programs; unconscious-bias training |

- **Joy Buolamwini** (Algorithmic Justice League): *"AI is not neutral. We have a responsibility to ensure it reflects the best of humanity, not the worst."* See [[algorithmic-bias]].

## 5. Assessing ethical impacts ([[ethical-impact-assessment]])

- **Why assess:** **79% of Americans** (Pew) believe tech firms must be held accountable for what they create. *"With great power comes great responsibility."*

### Ethical Impact Assessment (EIA), likely exam fodder
A structured way to evaluate ethical implications **before deployment**, analogous to an **environmental impact assessment**. Considers:
1. **Privacy + data security:** how is data collected, stored, shared; breach risk?
2. **Bias + fairness:** does the design avoid reinforcing discrimination?
3. **Social impact:** how does it affect different social groups; does it widen a divide?

- Adopters: **OpenAI** integrates EIAs to assess misuse/harm; **university ethics committees** give independent risk assessment that can affect funding.

### Social media accountability
- Platforms (Facebook, Twitter, YouTube) reshaped communication but spread **misinformation, hate speech, polarisation**. Cambridge Analytica reused here as the touchstone case; Zuckerberg testified to Congress repeatedly.
- **Assessment tactics:** **content moderation** (AI + human reviewers), **transparency reports** (what data/content handled and why), **independent third-party audits** (check algorithms for bias).

### Cautionary tale: Google's AI Ethics Council (2019)
- Set up to assess social/ethical impacts of AI, **dissolved within a week** after backlash over members' conflicting interests and controversial statements. **Lesson:** ethical oversight must be **transparent, diverse, and genuinely committed**; a committee alone solves nothing without a real plan to integrate ethics into development.

### Regulation
- **GDPR** (EU): explicit consent before collecting data; rights to **access and delete** data.
- **CCPA** (California Consumer Privacy Act): US step in the same direction; more still needed.

### Ethical frameworks to know
- **IEEE Ethics in Action**, **Google's AI Principles**, and APA guidelines for social-computing/usability questions. Familiarity with these is the professional duty.
- Sheryl Sandberg: *"we need to work together to ensure that our technology works for everyone, not just the privileged few."*

## 6. Employer voice: inclusivity in the workplace ([[inclusive-workplace-tech]])

An industry Q&A on inclusive workplace computing. Recurring practitioner advice:

| Theme | Practical steps |
|---|---|
| **Diverse perspectives** | (1) **Cultural training** tailored to company/industry/product; (2) involve diverse stakeholder groups via **co-design** or monitoring; (3) regular **cultural/societal audits** of usability across groups |
| **Legal/ethical risk** | Failing to account for diverse users → **legislative** and **reputational** damage; governance via **UK Equality Act**, **EU AI Act** |
| **Neurodiverse employees** | Train **HR + line managers** on neurodiversity (under-adopted in smaller firms); invest in **assistive tech** (text-to-speech, speech-to-text) and **customisable solutions** (in-house or vendor). Focus on **equity, not just equality** |
| **Monitoring / performance systems** | (1) **Algorithmic transparency**, explain metrics to employees; (2) **regular bias audits** with **human-in-the-loop**; (3) use **generative AI as an audit tool** to locate biases in hiring/performance pipelines |
| **Intersectionality** | Use an **intersectionality-by-design** approach (like security-/responsibility-by-design); analyse how race/gender/disability are catered for; combine **inclusive design** (principles + diverse team) with **feedback loops and phased rollouts** (pilot widely, update often) |
| **Digital literacy** | Upskilling is now as essential as basic literacy; build **tailored upskilling programs**; partner with **NGOs / community orgs** to reach underrepresented groups. Lack of digital fluency *is* an ethical issue. Diversity is profitable for individual, employer, and end users |

- **Key idea:** shift from **equality** to **equity**, treat lack of digital fluency among underrepresented groups as an ethical responsibility, and use phased releases to catch intersectional bias early.

## 7. Topic summary

Ethics and inclusivity are not buzzwords but core to tech that serves everyone. **Ethics** asks whether tech is used responsibly (privacy, data security, AI bias, social-media misinformation). **Inclusivity** designs for everyone through accessible interfaces, bias-free AI, and diverse user needs, so no one is left behind (the Xbox Adaptive Controller as the emblem). By holding ourselves accountable and designing with diverse needs in mind, we build tech that is innovative **and** responsible and fair.

## Related concepts
- [[inclusive-computing]], designing tech usable by the widest range of people
- [[accessibility]], usable by all abilities; universal design + the curb-cut effect
- [[universal-design]], TODO, design for one extends to many
- [[wcag]], Web Content Accessibility Guidelines (BBC iPlayer hit WCAG 2.1), TODO
- [[xbox-adaptive-controller]], modular accessible gaming hardware + misuse debate
- [[algorithmic-bias]], biased data → discriminatory AI (Amazon, facial recognition)
- [[ethical-impacts-of-technology]], privacy, bias, automation, digital divide
- [[digital-divide]], the access gap, exposed by COVID, TODO
- [[ethical-impact-assessment]], structured pre-deployment ethics review (EIA)
- [[inclusive-practices]], practitioner toolkit (design thinking, diverse teams, ARIA)
- [[inclusive-workplace-tech]], equity, neurodiversity, intersectionality-by-design
- [[data-protection-act-2018]], DPA 2018 / UK GDPR (cross-link to Topic 3)
- [[fair-use-doctrine]], TODO, cross-link to Topic 3 IP cases
- [[informed-consent]], the consent duty (cross-link to Topic 3)
- [[ada-domino-case]], TODO, ADA applies to digital platforms
- [[ai-fairness-360]], TODO, IBM bias-detection toolkit
