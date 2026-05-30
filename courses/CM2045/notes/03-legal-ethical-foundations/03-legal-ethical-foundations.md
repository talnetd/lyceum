# Topic 3: Legal and Ethical Foundations

> CM2045 · Topic 3 (Legal & Ethical Foundations) · 8 lectures
> Source transcripts: `notes/transcripts/03-legal-ethical-foundations/` (local, gitignored)

## TL;DR
**Ethics** (what's right, subjective, unenforced) and **law** (rules the state enforces) overlap but aren't the same: legal does not mean ethical. UK computing law is always **playing catch-up** with technology, the **Computer Misuse Act 1990** predates smartphones and the cloud; the **Data Protection Act 2018 / UK GDPR** still strains against AI. **Intellectual property** is the running theme: three case studies show copyright (Oracle v Google), patents (Apple v Samsung, patent trolls), and copyright in digital media (Napster, streaming, fair use) all swinging between **protecting** and **stifling** innovation. The topic closes on two professional duties: weigh **ethics** in design (the GeoTracks study: safety vs enjoyment vs autonomy vs privacy), shrink the **environmental cost** of computing (sustainable computing), and manage **legal risk** in IT projects (contracts, data, IP, compliance).

## 1. Computer ethics and UK law ([[ethics-vs-law]])

- **Ethics** = principles of right/wrong. Subjective, culture-dependent, usually no hard enforcement.
- **Law** = rules enforced by government; break them and there are sanctions.
- **Key tension: legal ≠ ethical.** Early web firms could harvest personal data *legally*, but was it ethical? **Cambridge Analytica** harvested Facebook data under the T&Cs (legal-ish) yet caused enormous ethical backlash, fuelling reform (DPA 2018, GDPR).

### UK legislation to know
| Law | Year | What it does | The catch-up problem |
|---|---|---|---|
| **Computer Misuse Act** | 1990 | Criminalises **unauthorised access** to computer systems ("hacking is bad") | Predates smartphones, social media, cloud |
| **Data Protection Act / UK GDPR** | 2018 | Governs how personal data is **collected, stored, used** | Strains against AI that predicts behaviour or gates loans/jobs | See [[data-protection-act-2018]] |

### Recurring ethical themes (likely exam fodder)
- **Privacy** (culturally relative: age, location, medical history sensitivity varies)
- **Security** and encryption backdoors (should law enforcement get them?)
- **Intellectual property** (how strict is too strict?)
- **Social responsibility / the digital divide** (are we widening or narrowing the access gap?)
- **Algorithmic bias** (facial recognition with higher error rates for people of colour: legal, but harmful and inequitable)
- **AI liability** (if an AI misdiagnoses or wrongly denies a claim, who's responsible: developer, company, machine?)
- **"Code is law"** (Lessig): software/algorithm design constrains freedom as much as Parliament does. See [[code-is-law]].

## 2. IP Case Study 1: Copyright, Oracle v Google ([[oracle-v-google]])

The landmark **API copyright** case.

- **2010:** Oracle (owner of Java via Sun acquisition) sues Google for reusing **37 Java API packages** in Android. Sought **~$9bn**.
- **Core question:** *Can APIs be copyrighted?* Oracle: yes (creative). Google: no, APIs are functional building blocks ("like keys on a keyboard / rules of grammar").
- Google copied only the **declaring code** (~11,500 lines: method names + structure/sequence/organisation), wrote its **own implementing code**, so Java devs' skills carried over to Android.

| Year | Court | Result |
|---|---|---|
| 2012 | District | **Google** wins, APIs too functional (typewriter-keys analogy) |
| 2014 | Federal Circuit | **Oracle** wins, APIs copyrightable, reuse not automatically fair use |
| 2021 | **Supreme Court** | **Google** wins on **fair use** (transformative; took only what was needed) |

- **Note:** SCOTUS decided the **fair-use** question and *sidestepped* whether all APIs are copyrightable, so the broader question is still open.
- Google's reuse was **deliberate** (it tried to licence Java first; the "Lindholm email" showed it knew a licence might be needed), but **intent doesn't defeat a fair-use defence**, transformativeness does. See [[fair-use-doctrine]].

## 3. IP Case Study 2: Software patents ([[software-patents]])

- A **patent** = exclusive rights to an invention, ~**20 years**; in software it protects a process/method/functionality. In exchange the inventor **discloses** the invention publicly.
- **Tension:** patents are designed for physical inventions, software is "just" algorithms. Should an obvious idea, or one many devs could independently invent, be patentable?

### Timeline + key cases
| Milestone | Year | Significance |
|---|---|---|
| **Diamond v Diehr** | 1981 | SCOTUS: a computer-implemented process *can* be patented if tied to a physical process, opens the floodgates |
| 1990s | | Software patents skyrocket |
| **Apple v Samsung** | 2012 | Apple wins **$1bn** over UI patents (bounce-back/rubber-banding, tap-to-zoom); critics: these are too obvious to patent |
| **Alice Corp v CLS Bank** | 2014 | SCOTUS: implementing an **abstract idea** on a computer isn't patentable, invalidates thousands of patents |

### The debate
- **Pro:** recoup R&D, stop free-riding copycats (e.g. **Qualcomm**'s thousands of wireless patents).
- **Anti:** **patent trolls** (hold patents to sue, not build, e.g. **Uniloc** suing MS/Google/Apple); broad/generic patents are a "legal minefield" for small devs (e.g. one-click-purchase button).
- **Alternative:** **open-source licences** (Linux thrives with no patents). See [[open-source-licensing]].
- **International divergence:** US tightened (Alice); Japan/Germany more lenient, no unified global standard.

## 4. IP Case Study 3: Copyright in digital media ([[copyright-digital-media]])

- **Copyright** = exclusive rights to copy/distribute/adapt an original work; lasts **life + 70 years** (most countries). Written pre-internet, now anyone can copy/share in seconds.
- **Piracy arc:** **Napster** (Metallica sued it) → Kazaa/BitTorrent → est. **$12.5bn/yr** US music-piracy loss (2007 IPI study) → industry pivots to **streaming** (Spotify, Apple Music).
- **Streaming's new fight, fair pay:** Taylor Swift pulled her catalogue from Spotify (2014) over low per-stream pay.
- **User-generated content:** YouTube's **Content ID** auto-flags rights-holders' material, criticised for penalising brief/incidental/fair use ("Russian roulette with your content").
- **Remix culture battle:** fan fiction/remixes are technically unauthorised derivatives. Lessig: *"the law demands the permission of the past to build the future."* TikTok/SoundCloud negotiate licences to enable legal derivatives.
- **Fair use:** limited use without permission for commentary/criticism/parody, a lifeline for reviewers/streamers, but **boundaries are vague**. See [[fair-use-doctrine]].
- **Jurisdiction clash:** EU **Article 17** (ex-Article 13) forces platforms to filter copyrighted content (critics: stifles speech) vs more lenient US fair use. **Creative Commons** offers a middle path. See [[creative-commons]].

## 5. Ethical decision-making: the GeoTracks study ([[ethical-tradeoffs-in-design]])

A real study of **adaptive music** that changes with your GPS location (e.g. simplifies/quietens the mix near a busy road). A worked example of design ethics:

- **Safety vs immersion:** music can dangerously block out traffic. Mitigation: **bone-conduction (jawbone) headphones** keep ear canals clear so users still hear surroundings.
- **Enjoyment vs safety:** simplifying tracks near hazards frustrated users ("my favourite part got skipped"), how far can you alter music before it stops being enjoyable?
- **Autonomy vs safety (paternalism):** the system adapted **automatically** with no user override. Do we prioritise user control or protect them, even by removing control?
- **Real-world unpredictability:** an emergency vehicle during a crossing created risk the system couldn't accommodate; lesson, let participants learn the route *without* music first.
- **Privacy:** GPS = real-time location data. Who can access it, how long is it kept, breach risk? The study **anonymised/coded** interview data and locked the USB away. Users must give **informed consent**. See [[informed-consent]].

**Takeaway:** designing tech that touches the real world means continuously trading off **safety, enjoyment, control, and privacy**, there's rarely a clean win.

## 6. Sustainability and ethics in computing ([[sustainable-computing]])

*(Parts 1 & 2 flattened.)* Computing is **energy-thirsty**, and the bill is environmental, not just financial.

### The scale of the problem
- Data centres use **~200 TWh/yr** (≈ Argentina's electricity); ICT could hit **~4% now → up to 14% of world energy by 2040** (Gartner).
- Data centres emit **~2–3% of global CO2**, on par with **aviation**.
- Training one large model (**GPT-3**) ≈ **284 tonnes CO2** ≈ five cars over their lifetimes.
- **Water:** Microsoft's Quincy WA data centres used **>250M litres** in 2020 (cooling).
- **E-waste:** **57M tonnes in 2021** (≈ 4,500 Eiffel Towers).
- **Bitcoin mining** consumes more electricity annually than **Sweden**.

### Sustainable practices (and their trade-offs)
| Practice | Idea | Catch |
|---|---|---|
| **Green data centres** | Run on renewables (Google/MS 100% renewable pledges) | none |
| **Energy-efficient hardware** | ARM chips, NVIDIA DGX-A100 (~30% less power) | none |
| **Dynamic resource allocation** | Serverless/edge: power only when needed | none |
| **Green AI** | Smaller models, **transfer learning** | Accuracy/effort balance |
| **Circular computing** | Recycle/refurbish/repurpose hardware (Dell Optiplex from recycled plastics) | Demand for new devices keeps rising; Apple criticised for hard-to-repair designs |
| **Carbon offsetting** | Buy carbon credits | Not a real fix, just mitigation |
| **Greener crypto** | Chia's **Proof of Space and Time** (uses spare disk) | Wears out drives faster → more **e-waste** |

- **AI cuts both ways:** huge training cost, but Google uses ML to cut data-centre **cooling energy by ~40%**, and ML aids climate science (deforestation, weather, grid optimisation).
- **Ethical question:** is it right to prioritise compute over the planet, and how do we ensure clean tech benefits everyone, not just those who can afford it? See [[e-waste]], [[green-ai]].

## 7. Handling legal risks in IT projects ([[legal-risk-management]])

**Legal risk** = anything that could cause financial loss, disputes, fines, or reputational damage from failing to comply with law.

### The four common risk types
1. **Contract disputes** (unclear scope/deliverables/timelines)
2. **Data privacy & security** (GDPR non-compliance, breaches)
3. **IP issues** (who owns the software/algorithm?)
4. **Compliance** with industry standards (healthcare, finance)

### Case studies (note the callbacks)
| Case | Risk type | Outcome / lesson |
|---|---|---|
| **NHS National Programme for IT** (2002–2011) | Contract | Ballooned to **£12bn**, scrapped, *poorly defined contracts → disaster* |
| **Facebook / Cambridge Analytica** (2018) | Data privacy | **$5bn FTC fine**, accelerated GDPR; *handle data lawfully + ethically* |
| **Oracle v Google** (2010–2021) | IP | Google's API reuse = **fair use**; *negotiate/licence IP properly* |

### Protections + best practices (exam checklist)
- **Protections:** comprehensive contracts (with change management), **IP ownership agreements**, data-protection compliance (GDPR/CCPA + processor agreements), **liability clauses**.
- **Best practices:** involve **legal teams early**, run **regular audits**, **document everything**, **train teams**.
- **Emerging frontiers:** AI (bias, autonomous-decision liability), blockchain, quantum, frameworks still forming.

## Related concepts
- [[code-is-law]], Lessig: design as regulation
- [[data-protection-act-2018]], DPA 2018 + UK GDPR
- [[fair-use-doctrine]], the transformative-use defence (ties cases 1 & 3)
- [[oracle-v-google]], API copyright
- [[software-patents]], patents, trolls, Alice/Diehr
- [[copyright-digital-media]], piracy, streaming, Content ID
- [[open-source-licensing]], the patent alternative
- [[creative-commons]], flexible licensing
- [[ethics-vs-law]], legal ≠ ethical
- [[informed-consent]], the privacy/consent duty
- [[sustainable-computing]], energy, water, e-waste trade-offs
- [[green-ai]], TODO
- [[e-waste]], TODO
- [[legal-risk-management]], IT-project legal hygiene
- [[computer-misuse-act-1990]], TODO
