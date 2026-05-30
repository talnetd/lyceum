# Topic 7: Industry Standards

> CM2045 · Topic 7 (Industry Standards) · 5 lectures
> Source transcripts: `notes/transcripts/07-industry-standards/` (local, gitignored)

## TL;DR
A **standard** is a documented agreement of technical specifications used consistently as rules/guidelines so products, processes and services are fit for purpose (think the light-bulb fitting that works in any lamp). Standards deliver **interoperability, safety, efficiency, innovation and consumer protection**; when absent or bad they cause **incompatibility, security risks and stifled innovation**. Standards are either **de facto** (dominant in practice via market forces, e.g. QWERTY, Windows) or **de jure** (formally approved by a body, e.g. GSM, IEEE 802.11, ISO 27001), and de facto often becomes de jure. The key bodies are **IEEE** (electrical/electronics/computing), **ISO** (cross-industry, e.g. ISO 9001), **W3C** (HTML/CSS/XML), and **IETF** (internet via **RFCs**), with **NIST** and the **ACM** also influential. The lifecycle anchor is **IEEE 12207** (software lifecycle processes); the cautionary case studies (**Mars Climate Orbiter**, **Ariane 5**, **Y2K**, **Heartbleed**) show what ignoring standards costs. **Security best practice** layers defences (client, server, network, data) and is framed by **ISO/IEC 27001**, **IEEE 802.11i** and **NIST**.

## 1. What a standard is and why it matters ([[industry-standards]])

- **Standard** = a documented agreement containing technical specifications or precise criteria, used consistently as rules, guidelines or definitions of characteristics, to ensure materials, products, processes and services are **fit for purpose**.
- Standards work invisibly to deliver **interoperability, safety and efficiency**; the light-bulb fitting analogy: the standard fitting means any compliant bulb works in any compliant lamp.

### Value standards add (likely exam fodder)
| Value | What it means |
|---|---|
| **Interoperability** | Different systems/devices work together seamlessly |
| **Safety** | Products/services meet minimum safety requirements |
| **Efficiency** | Efficient use of resources, less waste |
| **Innovation** | A common foundation to build and develop on |
| **Consumer protection** | Guarantees a baseline of quality and performance |

### When standards go wrong (likely exam fodder)
- **Incompatibility:** e.g. a charger that only works with one phone model.
- **Security risks:** poorly designed security standards leave systems open (the **Heartbleed** bug in OpenSSL).
- **Stifled innovation:** overly restrictive standards limit experimentation.

## 2. Standards bodies and document types ([[standards-organisations]])

| Body | Full name | Domain / examples |
|---|---|---|
| **IEEE** | Institute of Electrical and Electronics Engineers | Electrical, electronics, computing: Wi-Fi **802.11**, Ethernet **802.3** |
| **ISO** | International Organisation for Standardisation | Cross-industry (manufacturing, healthcare, tech): **ISO 9001** quality management |
| **W3C** | World Wide Web Consortium | Web standards: **HTML, CSS, XML** |
| **IETF** | Internet Engineering Task Force | Internet standards via **RFCs** (Request for Comments) |
| **NIST** | National Institute of Standards and Technology (US) | Cryptography, risk management; globally influential |
| **ACM** | Association for Computing Machinery | With IEEE, one of the two key institutions for accessible computing information |

- **RFC (Request for Comments):** a formal IETF document proposing/defining an internet standard, produced by an **open, collaborative consultation process** (hence "comments").

### Examples of standards in computing (likely exam fodder)
- **TCP/IP:** the fundamental communication protocol of the internet (without it the internet as we know it could not exist).
- **HTML:** the standard markup language for web pages (no standard = browsing chaos).
- **IBM PC:** IBM used off-the-shelf components and **published specifications**, driving widespread adoption and the modern PC industry.

### Core computer science standards
| Area | Standard examples | Purpose |
|---|---|---|
| **Data encoding** | ASCII, Unicode | Consistent character/symbol representation across systems |
| **Programming languages** | C++, Java, Python | Define syntax/semantics so code is shareable and portable |
| **Data structures** | arrays, linked lists, trees | Standardised ways to organise and store data efficiently |
| **Algorithms** | sorting, searching, encryption | Well-defined procedures for common computational problems |

## 3. De facto vs de jure standards ([[de-facto-vs-de-jure]])

Two contrasting ways something becomes a "standard" (likely exam fodder):

| Type | Meaning | How it arises | Examples |
|---|---|---|---|
| **De facto** | "in fact / in practice" | Widely adopted organically via market forces and user preference; not formally approved | **QWERTY** keyboard layout, **Microsoft Windows** (desktop OS) |
| **De jure** | "by law / according to law" | Officially recognised/approved by a body or government via a formal process of experts and stakeholders | **GSM** (mobile), **IEEE 802.11** (Wi-Fi), **ISO 27001** (infosec management) |

- **Key dynamic:** many standards **start as de facto and become de jure** through the formal standardisation process.
- **Format wars** show market forces decide adoption: **VHS beat Betamax** (despite being arguably technically inferior), **DVD beat CD** (more storage), **Blu-ray** then overtook on fidelity/capacity. Backward compatibility and consumer adoption matter as much as technical merit.

## 4. The IEEE ([[ieee-standards]])

- Global body, **400,000+ members across 160 countries**; offers **student/graduate membership** with access to resources like the IEEE library.
- Founded **1884 as the AIEE**, mission: **advancing technology for the benefit of humanity**.
- Activities: developing standards, publishing technical literature, organising conferences, providing education.
- **Standards process is open and consensus-based:** anyone can participate; rigorous multi-stage review and approval ensures quality and fairness; adopted worldwide.
- Focus areas: electrical engineering (power, renewables, EVs), electronics (microelectronics, semiconductors, nanotech), computer engineering (architecture, software engineering, cyber security), **usability/accessibility**, telecommunications (wireless, networking, internet).

### IEEE 802 networking family (likely exam fodder)
| Standard | Name | Use |
|---|---|---|
| **802.3** | Ethernet | Foundation of wired networking; physical + data-link layers |
| **802.11** | Wi-Fi | Ubiquitous wireless networking |
| **802.15.1** | Bluetooth | Short-range wireless (headphones, keyboards, smart home) |

### Other notable IEEE standards (likely exam fodder)
| Standard | What it defines |
|---|---|
| **IEEE 754** | Format for **floating-point numbers** (consistent numerical computation) |
| **IEEE 1394** | **FireWire**, high-speed serial bus (cameras, external drives) |
| **IEEE 1076** | **VHDL**, hardware description language to design/simulate digital circuits |

- IEEE standards underpin emerging tech: **smart grid**, **autonomous vehicles**, **IoT** (smart homes/fridges, billions of connected devices).

## 5. Software lifecycle: IEEE 12207 ([[software-lifecycle]])

**IEEE 12207** maps the **software lifecycle**, the journey from idea to finished product and beyond. It defines **processes, not specifics**: it does not tell you how to code, it frames how development is organised. It is an **adaptable framework**, tailorable to project type/size, and even works alongside **agile**.

- **Why a lifecycle standard:** software is complex (e.g. air traffic control); diverse teams (programmers, designers, testers, project managers) need a **common language and framework**; it brings **consistency, quality and predictability**.

### Key processes (likely exam fodder)
| Process | What it covers |
|---|---|
| **Acquisition** | Figure out what the software needs to do, get resources, make a plan |
| **Supply** | Actually building the software (design, coding, testing) |
| **Development** | Core coding, plus documentation and reviews |
| **Operation** | Deploy, user support, keep it running |
| **Maintenance** | Fix bugs, add features, adapt to changing needs |

- **Structure:** processes contain **activities** (e.g. requirements analysis sits in acquisition), which break into **tasks**, each with defined **inputs and outputs**.
- **Documentation-heavy:** tracks progress, ensures consistency, transfers knowledge. Document types include requirements documents, design documents, test plans, user manuals. **Traceability** links documents/activities so connections are visible.
- **Benefits:** improved communication, reduced risk, higher-quality software, increased efficiency. Companies can be **certified** for compliance; useful for small teams too, not just large/critical systems.

## 6. Case studies: standards in (in)action ([[standards-case-studies]])

Real failures where missing or ignored standards caused harm; each maps to a standard that could have prevented it (likely exam fodder).

| Case | Year | Failure | Standard solution |
|---|---|---|---|
| **Mars Climate Orbiter** | 1999 | **$125M** spacecraft lost: one team used metric (Newtons), another imperial (pounds-force); orbiter hit the atmosphere at the wrong angle and burned up | Enforce a single unit system (**SI units**) project-wide |
| **Ariane 5 rocket** | 1996 | Exploded seconds after launch: code reused from **Ariane 4** forced a 64-bit number into 16-bit space, an **integer overflow** cascading into errors | Rigorous **code reviews**, data-type validation, conversion standards; move from unit to **integration testing** (A and B may each work, test them together) |
| **Y2K bug** | ~2000 | Systems stored years as **two digits** (99) to save space; rollover to 00 risked being read as 1900; inconsistent date formats and legacy banking/government code | **ISO 8601** date/time format (4-digit year, 2-digit month, 2-digit day), adopted and enforced early. Cost **billions** in remediation; impact softened by massive fixes |
| **Vulnerable web server (Heartbleed)** | 2017-era example | Server hacked via outdated **OpenSSL** with a known flaw (**Heartbleed**); user data exposed, financial + reputational damage | Follow security standards (**NIST**); patch/update regularly |
| **Tower of Babel (language sprawl)** | (lecturer's own project) | Multiple programming languages with no interoperability guidelines made inter-module communication hard, raising dev time and error risk | Clear **coding conventions**, **standardised APIs** between modules, ideally one language for core functionality |

- **Takeaway:** standards are not rules for their own sake; they prevent costly mistakes, ensure compatibility, and build reliable, secure systems. Y2K underlines the **long-term consequences of small decisions** and the need for foresight.

## 7. Security best practices ([[security-best-practices]])

Working software is only half the battle; it must also be **secure**. Don't invent security from scratch, use established frameworks (likely exam fodder).

| Standard | Scope |
|---|---|
| **ISO/IEC 27001** | Comprehensive **Information Security Management System (ISMS)**, a blueprint for security |
| **IEEE 802.11i** | Wi-Fi security; defines protocols like **WPA2 / WPA3** for wireless networks |
| **NIST** | US guidelines, globally influential, covering cryptography to risk management |
| **RFC 5322** | Email format/validation (example of an input-validation standard) |

### Defence in layers (likely exam fodder)
Good security has **layers**, making penetration harder. Check at multiple levels:

| Layer | Controls |
|---|---|
| **Validation level** | Secure coding to prevent **SQL injection** and **cross-site scripting**; input validation client-side and server-side. GDS guidance (e.g. splitting date of birth into day/month/year) reduces accidental errors and aids **accessibility** |
| **Network level** | Firewalls, intrusion detection systems, secure network configuration |
| **Data level** | **Encryption** in transit (HTTPS) and at rest (encrypted databases); **access control** so only authorised users see sensitive data |

### ISO 27001 as the foundation
- Not just tech: a **holistic** approach spanning **policies, procedures and employee training**.
- **Risk assessment:** identify assets to protect and the threats against them; this guides measures.
- **Control selection:** ISO 27001 offers a catalogue of controls (access control, cryptography, physical security) chosen by risk.
- **Continuous improvement:** regularly review and update to meet new threats.

### Security case studies
| Case | Lesson |
|---|---|
| **Equifax breach (2017)** | Failure to fix a **known vulnerability** exposed millions of records, vulnerability management and adherence to standards matter |
| **GDPR compliance** | EU mandates strong data protection; implementing **ISO 27001** helps organisations comply |
| **Secure online banking** | Layered security: strong **multi-factor authentication**, encryption, fraud detection |

- **Bottom line:** standards provide the roadmap, but it's on practitioners to implement them effectively and keep adapting; standardisation keeps things predictable and mitigates risk.

## Related concepts
- [[industry-standards]], what standards are, value, and failure modes
- [[standards-organisations]], IEEE, ISO, W3C, IETF, NIST, ACM and RFCs
- [[de-facto-vs-de-jure]], practice-driven vs legally/formally approved standards
- [[ieee-standards]], the IEEE body and its 802 / 754 / 1394 / 1076 standards
- [[software-lifecycle]], IEEE 12207 processes (acquisition → maintenance)
- [[standards-case-studies]], Mars Orbiter, Ariane 5, Y2K, Heartbleed
- [[security-best-practices]], layered defence + ISO 27001 / 802.11i / NIST
- [[iso-27001]], TODO, ISMS blueprint (risk assessment, controls, improvement)
- [[iso-8601]], TODO, unambiguous date/time format (the Y2K fix)
- [[ieee-754]], TODO, floating-point number representation
- [[tcp-ip]], TODO, the internet's fundamental protocol
- [[integration-testing]], TODO, testing components working together (Ariane 5 lesson)
- [[heartbleed]], TODO, the OpenSSL vulnerability
