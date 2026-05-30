# Topic 6: Risk Management & Security

> CM2045 · Topic 6 (Risk & Security) · 5 lectures
> Source transcripts: `notes/transcripts/06-risk-security/` (local, gitignored)

## TL;DR
The whole topic turns on one tension: **accessibility vs security**. Open, user-friendly systems are exactly the systems attackers can walk into, so **risk management** means being **proactive not reactive**, identifying hazards then assessing their **likelihood and impact**. Three levers recur: **policy** (who gets access to what, when, how), **technology** (MFA, encryption, EDR, SIEM, intrusion detection), and the **human element**, which is the **weakest link** (sticky-note passwords, phishing clicks). Threats range from **malware/ransomware/DoS** to **social engineering**, **insider threats**, and **supply-chain attacks** (the **SolarWinds** "contaminated flour" case). **Frameworks** (**NIST**, **ISO 27001**) are the toolkits that standardise this work on a **risk-based approach** (don't over-control where there's no risk). **NIST** (US National Institute of Standards and Technology) sets the common-language **Cybersecurity Framework** (likely heavily tested). A good **incident response plan** rests on identified **critical assets**, a clear **policy**, training, and modern tooling. The **employer voice** (Carlos Russell, Ternium) reframes cyber as a **board-level operational risk** demanding **resilience**, **continuous end-to-end monitoring**, **third-party/supply-chain certification**, **quantitative ($) risk**, **privacy compliance**, and **ethics/explainability**, with **AI** and **quantum** as the next disruptors cutting both ways.

## 1. Risk management fundamentals ([[risk-management]])

- **Risk management** = identify potential hazards, assess their **likelihood** and **impact**, then plan the response. Be **proactive, not reactive**: anticipate threats before they knock.
- **Core tension (likely exam fodder): accessibility vs security.** Every opening that makes a system open and usable is a potential way in for cybercriminals. The job is to strike the **balance**, a constant negotiation between **convenience and protection**.
- Three pillars that run through every lecture:
  - **Policy**, the rulebook: who has access to what, when, and under what conditions. A robust policy is the **first line of defence**.
  - **Technology**, the controls (see section 2).
  - **People**, the **human element**: the weakest link.

### The human element (likely exam fodder)
- You can have the strongest firewalls and intrusion detection, but a password on a sticky note, or one click on a **phishing** email, undoes it.
- Mitigation is not technical: **educate, train, raise awareness**. Make everyone understand good security practice.

## 2. Cybersecurity fundamentals ([[cybersecurity-fundamentals]])

### Threats (the usual suspects)
- **Viruses, malware, ransomware**, plus **denial-of-service (DoS)** and **social engineering**.
- **Insider threat**: the unhappy employee or the accidental data leak. Threats are **intentional or accidental**, and both matter.
- **Quantum computing** could render current **encryption** obsolete (a forward-looking threat, see section 5).

### Controls and principles
| Control / principle | What it does |
|---|---|
| **Multi-factor authentication (MFA)** | Extra factor beyond a password to keep attackers out |
| **Encryption** | Scrambles data so it's useless if intercepted |
| **Penetration testing** | Probes systems for weaknesses before attackers do |
| **Mobile device management (MDM)** | Manages/secures mobile endpoints |
| **Endpoint detection & response (EDR)** | Detects "sneaky" attacks on endpoints |
| **Principle of least privilege** | Give just enough access to do the job, no more. See [[principle-of-least-privilege]] |
| **Separation of duties** | Split critical tasks so no one person holds "the keys to the kingdom" |

### UNIX permissions as a least-privilege example (likely exam fodder)
The lecture uses `chmod 755` to make least privilege concrete:
- **755**: **owner** gets read + write + execute (full access); **group** and **others** get read + execute only.
- Mapping intent to permission: need to **edit a config file** → grant **write**; only need to **run a script** → **read + execute** is enough.
- The point is conceptual, not the octal: grant the minimum access the task requires.

## 3. Risk management frameworks ([[risk-management-frameworks]])

Frameworks are the **toolkits**: they provide tools/techniques to **assess risk**, **implement controls**, and **ensure compliance** with industry standards. You don't need to memorise the standards verbatim, but know their role.

| Framework | Origin | Role |
|---|---|---|
| **NIST** (esp. the Cybersecurity Framework) | US (National Institute of Standards and Technology) | Common language + standards for managing cyber risk. See [[nist-framework]] |
| **ISO 27001 / ISO 27000-series** | International (ISO) | Best-practice approach to managing cybersecurity as a function; depth/detail needed to protect a business |

- Apply frameworks on a **risk-based approach**: don't **overshoot controls where there's no risk**, aim for the **right balance**.
- Adopting a framework lets you **assess the maturity** of your own programme and build a **remedial / continuous-improvement plan**.

## 4. NIST and its purpose ([[nist-framework]]) (likely exam fodder)

**NIST = National Institute of Standards and Technology** (US). The lecturer flags this as the key standards body, expect it tested.

- NIST develops **standards, guidelines, and best practices** across many fields (cybersecurity through to measurement science).
- **Why it matters:** without NIST there would be **no consistency, no interoperability, just confusion**. NIST guidance sits alongside laws like the **Computer Misuse Act** and **GDPR** to define **best practice**.
- The **NIST Cybersecurity Framework** is a "digital handbook": it provides a **common language** and a **set of standards** for managing cybersecurity risk so organisations can **understand each other and work together** to reduce cybercrime.
- In **risk management** specifically, NIST gives guidance on how to **identify, assess, and mitigate** risks, understand vulnerabilities, and develop protective strategies.
- NIST is also **forward-looking**: researching new technologies and developing new standards for tomorrow's challenges.

> Exam framing: NIST is "the rulemaker / guardian of the digital ecosystem", its **purpose** is **consistency, interoperability, a common security language, and risk-management guidance**.

## 5. Incident response planning ([[incident-response]])

An **incident response plan** safeguards an organisation's vital assets and keeps it **operationally continuous** under digital attack. It rests on the same three pillars (risk, policy, people) plus tooling.

### Foundational steps (do these before writing the plan)
1. **Identify critical assets**: what data/systems/services are essential? (e.g. research data, student records, financial systems).
2. **Assess the risks** they face: what threats, how likely, what impact? This **risk assessment** is the basis of the strategy.

### The plan itself
| Element | Why it matters |
|---|---|
| **Clear, concise policy** | Defines **roles, responsibilities, procedures**; the "organisational flowchart for when the digital alarms ring", ensuring a **coordinated, consistent** response |
| **Training & awareness** | Human error (phishing, weak passwords, lost laptops) still exposes you despite good tools |
| **Detection / response tooling** | **Intrusion detection systems (IDS)**, **SIEM** (Security Information and Event Management), and **threat-intelligence platforms** to detect, analyse, and respond in real time |
| **Automation & AI (looking ahead)** | Analyse vast data, spot patterns, automate responses for faster reaction |

### Case studies to cite
| Incident | Year | Lesson |
|---|---|---|
| **University of California ransomware attack** | 2020 | Academic institutions are vulnerable; you need a **well-rehearsed** incident response plan |
| **SolarWinds supply-chain attack** | 2020 | A trusted **software supplier** was compromised, so **one** poisoned update reached **thousands** of organisations (incl. major government agencies). See [[supply-chain-attack]] |

**The "contaminated flour" analogy (SolarWinds):** SolarWinds = the trusted flour supplier; a routine **software update** = the flour, secretly **contaminated** with malicious code; the companies/agencies = bakeries that unknowingly "baked" (installed) it; their users/victims got "sick" (data stolen, communications spied on). Significance: it was a **supply-chain attack** (hit a trusted supplier to compromise many at once), **highly sophisticated** (well-hidden code), and **wide-reaching**, it makes you "question everything" you trust in your supply chain.

## 6. Employer voice: cybersecurity in practice ([[employer-voice-cybersecurity]])

**Carlos Russell, Director (cybersecurity & compliance), Ternium** (steel manufacturing, Latin America). Practitioner takeaways:

- **Threats are getting more lethal with AI.** **Malware, phishing, ransomware** combined with **AI-powered attacks**: emails and social-media messages are now so well-drafted that people can't tell they're fake. Awareness training has to **raise the bar**.
- **Supply-chain / software risk is newer and huge.** Open-source and third-party libraries outside the dev team's control can carry a **backdoor** enabling remote ransomware. Question: how do you **certify your software supply chain**? Also **third-party risk**: vendors must subscribe to a **sustainable level of cybersecurity**, automotive supply chains now certify end-to-end for **both ESG (lower carbon) and data protection**.
- **Frameworks, pick from plenty.** **NIST** (US) and **ISO 27000-series** help **assess maturity** and build improvement plans, always **risk-based** (right balance, don't over-control).
- **Continuous, end-to-end monitoring.** Pre-pandemic the worry was the **external-facing** perimeter (firewalls + **SIEM** for event correlation). Now it must be **permanent, internal + external, inbound + outbound**, with **automation/AI** to detect **anomalies** that aren't obvious.
- **Cyber is now a board issue (likely exam fodder).** For US-listed businesses (NYSE/US exchanges), the **board** is expected to **supervise** the cyber programme, not just the CIO/CFO. You must **translate technical risk into business risk** and give the board tools to oversee it.
- **Quantify risk in money, not just high/medium/low.** Regulation (for listed firms) now requires a **quantitative ($) impact** of disruption, disclosed to regulators. A "new skill" for the cyber function (we are "not actuaries").
- **Resilience is expected.** Prevent disruption where possible; if it happens, **recover fast** and keep impact small. Ask for help to recover if needed.
- **Privacy and compliance go hand in hand with cyber.** Strong **privacy laws** (Europe and beyond) mean protecting **people's data**: employees, patients, and especially **biometric data** (face/fingerprint), which is highly sensitive and damaging if leaked.
- **Emerging tech cuts both ways.**
  - **AI**: force for good (e.g. analysing **camera feeds to prevent danger to people**) but also enhances attackers (better phishing, **data-feed poisoning** that corrupts business decisions). Needs a **holistic risk-management approach** and **explainability** (a core requirement of the **EU AI Act**).
  - **Quantum computing**: huge processing power, opportunity and threat. It can **break cryptography**, so data we assumed safe (financial, medical) may not be. Track **post-quantum cryptography**. Stay informed about what's coming.
- **Social engineering is still rife**, and AI-empowered. The target is the **person**: faked conversations, **deepfake** voice/video (e.g. a fake "urgent" video of your CEO asking you to act) used to gain unauthorised access or commit fraud.
- **Ethics is at the core.** Humans supervise the AI toolkits and the risk decisions. "Deploying technology to do evil is an ethical decision going bad." Aim for **transparency** over **security by obscurity**; be transparent about the level of control needed for the level of risk faced.

## Related concepts
- [[risk-management]], proactive identify/assess (likelihood × impact)/plan; the accessibility-vs-security balance
- [[cybersecurity-fundamentals]], threats (malware, ransomware, DoS, social engineering, insider) and controls (MFA, encryption, pen-testing, EDR, MDM)
- [[principle-of-least-privilege]], grant minimum access; UNIX `chmod 755` example
- [[risk-management-frameworks]], the risk-based toolkit; NIST + ISO 27001
- [[nist-framework]], NIST Cybersecurity Framework: common language, consistency, interoperability (heavily tested)
- [[incident-response]], identify critical assets → assess risk → policy/roles → train → IDS/SIEM/threat-intel
- [[supply-chain-attack]], SolarWinds "contaminated flour"; trusted-supplier compromise
- [[employer-voice-cybersecurity]], Carlos Russell / Ternium: cyber as board-level operational risk
- [[cia-triad]], confidentiality / integrity / availability, TODO (standard security model underpinning the controls above)
- [[social-engineering]], manipulating people for unauthorised access; AI/deepfake-empowered, TODO
- [[post-quantum-cryptography]], crypto resilient to quantum attack, TODO
- [[siem]], Security Information and Event Management; event correlation, TODO
- [[computer-misuse-act-1990]], TODO (cited alongside NIST/GDPR as best-practice context)
