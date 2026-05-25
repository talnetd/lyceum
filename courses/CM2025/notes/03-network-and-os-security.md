# Topic 3: Network and OS Security

> CM2025 · Weeks 5-6, Topic 3 · 7 lectures
> Source transcripts: `notes/transcripts/03-network-and-os-security/` (local, gitignored)

## TL;DR
Networks and operating systems both work in **layers**, and so does the defence built around them. Firewalls filter traffic at the edge (stateless ACL, stateful, or proxy). **IDS** spots intrusions and alerts; **IPS** sits inline and blocks them. **Access control** decides who gets to what, four classic models trade flexibility for security (**DAC**, **MAC**, **RBAC**, **ABAC**). The OS itself is a major attack surface, fix that with **hardening**: patch, lock down configuration, remove unneeded software, and run audit tools like Harbian against Linux.

## 1. Networks, operating systems, and layered communication ([[osi-tcp-ip-models]])

A **network** = system of connected devices sharing data via IP addresses and protocols like TCP/IP. An **operating system** = software that manages hardware, runs programs, handles files/memory/input, and provides networking services.

Both build communication as a **stack of layers**: each layer talks only to its immediate neighbours and relies on what's below.

### Two layered models

| OSI (7 layers, teaching/design) | TCP/IP (4 layers, real systems) |
|---|---|
| 7. Application (browser, email) | Application (HTTP, SMTP) |
| 6. Presentation (formats, encryption) | (folded into Application) |
| 5. Session (conversation mgmt) | (folded into Application) |
| 4. Transport (TCP/UDP) | Transport |
| 3. Network (IP routing) | Internet |
| 2. Data link (frames) | Network interface |
| 1. Physical (cables, Wi-Fi signals) | (folded into Network interface) |

### How OS and network stack interact (loading a web page)
1. Browser (OS app layer) creates request.
2. **OS kernel** checks permissions, applies security policies.
3. **Transport** (TCP) breaks data into segments, adds port numbers.
4. **Internet** (IP) adds destination IP.
5. **Network interface** (Ethernet/Wi-Fi) converts to signals, sends.
6. On the receiver, same in reverse, signal → IP → TCP → app.

The OS is the **bridge** between user software and the network stack.

### Why layers matter for security
- Pinpoint **where** an attack lives (app-layer XSS vs network-layer DDoS).
- Decide where each control sits (firewall, IDS, encryption).
- Explain how malware moves laterally.
- Trace and block suspicious traffic.

> Understand the layer → know where to defend.

## 2. Firewalls ([[firewall]])

A firewall enforces rules on traffic crossing a boundary. Three classic types:

| Type | How it works | Trade-off |
|---|---|---|
| **Stateless (ACL)** | Inspects every packet independently against a rule set | Simple, but inefficient on big networks; no awareness of conversations |
| **Stateful** | Tracks connections; once a session is allowed, lets subsequent packets flow without re-checking | More efficient, slight overhead to track state; better for high-throughput |
| **Proxy** | Internal devices never talk directly to the outside; the proxy fetches on their behalf | Strongest isolation; proxy itself must be hardened |

### How a stateless ACL applies rules
Typically defaults to **deny all**, then allows specific traffic:
- "Allow packets to IP X"
- "Allow packets to port Y"
- ...

### Why proxy firewalls are powerful
External world only sees the proxy. You can harden the proxy heavily (patched, scanned, monitored), and the LAN is shielded from direct contact with the WAN.

## 3. Intrusion Detection Systems (IDS) ([[ids]])

> A system that runs on a network (or single machine) to detect when an intruder has entered.

**Why we need IDS**: "Most security experts agree that a completely secure system is impossible." You harden as much as you can, then assume some attacks will still get through.

### Core principle (Dorothy Denning, 1987)
> Exploitation of a system's vulnerabilities involves **abnormal use** of the system; therefore security violations can be detected from abnormal patterns of usage.

So an IDS is fundamentally a **pattern recognition** problem.

### Key challenges
- **False positives**: alerts on benign activity, wastes responder time.
- **False negatives**: misses real intrusions (usually the worse failure).
- **Performance**: must not slow the network down.
- **Scalability**: must work over distributed, cloud, containerised networks.

### Technology arc
| Era | Technique |
|---|---|
| 1980s | **Expert systems** (symbolic AI), e.g. Denning's IDES |
| 2010s+ | **Deep learning**, e.g. LSTM networks (recurrent), good at time-series patterns over a sequence of network events |

### Datasets
Public IDS datasets (Kaggle, GitHub) contain packet metadata + activity labels (normal, neptune, smurf, ...). Used to train and benchmark detectors.

### Commercial examples
| Vendor | Style |
|---|---|
| **Cisco** | Hardware appliance; signature/pattern downloads, doesn't advertise ML |
| **Darktrace** | Software; markets itself as ML/AI-driven, cloud-backed |

## 4. Intrusion Prevention Systems (IPS) ([[ips]])

An IPS does what an IDS does **plus** takes action: it sits **inline** (all traffic passes through it) and can drop packets, block connections, or reset sessions.

### IDS vs IPS

|  | **IDS** | **IPS** |
|---|---|---|
| Position | Out-of-band (mirror traffic) | **Inline** |
| Action | Detects + alerts | Detects + **blocks** |
| Analogy | Security camera | Security guard |
| Risk if misconfigured | Noise (alerts) | Blocked legitimate traffic |

### Detection techniques
| Technique | What it does |
|---|---|
| **Signature-based** | Matches known attack patterns (like antivirus) |
| **Anomaly-based** | Flags deviations from baseline (unusual logins, traffic spikes) |
| **Policy-based** | Enforces admin-defined rules |
| **Hybrid** | Combines all of the above; most modern IPS |

### Where IPS is deployed
- Between the firewall and the internal network.
- Protecting key assets (data centres, cloud).
- Built into a **Next-Generation Firewall (NGFW)**.

### Pros and cons

| Benefits | Limitations |
|---|---|
| Blocks at the edge before threats reach servers | False positives can block legitimate users |
| Catches known malware, zero-days, suspicious behaviour | Needs frequent signature/rule updates |
| Reduces load on internal defences | Becomes a bottleneck if under-provisioned |
| Supports GDPR/PCI DSS compliance | Not a replacement for firewalls, antivirus, training |

## 5. Access control models ([[access-control-models]])

Access control = who can access what, when, and how. Four models, ordered roughly by flexibility:

| Model | Who decides | Best for | Flexibility | Security |
|---|---|---|---|---|
| **DAC** (Discretionary) | The resource **owner** chooses | Personal computers, file-sharing | High | Low |
| **MAC** (Mandatory) | The **system**, via classifications (confidential, secret, top secret); users can't change | Military, government | Low | High |
| **RBAC** (Role-based) | Permissions follow the **job role** (manager, finance, sysadmin) | Enterprises (scales with org growth) | Medium | Medium |
| **ABAC** (Attribute-based) | Multiple attributes (role + time + location + device + sensitivity) | Cloud, large dynamic environments | High | High |

> Note: confusingly, **RBAC** sometimes appears in literature as "rule-based" rather than "role-based". In this module's lecture both names are used, but the meaning here is role-based.

### Why access control matters
- Protects sensitive data.
- Minimises insider-threat impact (combine with [[least-privilege]]).
- Helps meet GDPR, HIPAA.
- Prevents accidental access mistakes by staff.

## 6. OS hardening, Windows ([[os-hardening]])

OS security = preserving **confidentiality, integrity, availability** of the OS.

### Why it matters
Most systems are internet-facing today. Convenience (remote work, online services) creates exposure. Windows dominates desktops, so it's a big target. **70% of attacks in 2018 exploited MS Office vulnerabilities** (Kaspersky), via zero-day exploits in Word/Excel/Outlook documents.

### Key Windows security components
| Component                            | Role                                                                 |
| ------------------------------------ | -------------------------------------------------------------------- |
| **Security Reference Monitor (SRM)** | Kernel-mode permission checks, audit-log entries, privilege handling |
| **Local Security Authority (LSA)**   | Enforces local security policy; issues authentication tokens         |
| **Security Account Manager (SAM)**   | DB of user credentials and per-user/per-group data                   |
| **Active Directory**                 | Identity, encryption, policy across Cloud + on-prem                  |
| **WinLogon / NetLogon**              | Local logins / network logins                                        |

### Client-side vulnerabilities to know
- Web browsers (top targets get the most attacks).
- Office software (esp. MS Office: Word, Excel, Outlook).
- Email clients.

### Hardening steps (Windows)
- Disable automatic login.
- Require login to dismiss screensaver.
- Enable system security features (Defender, BitLocker, etc.).
- Disable wireless if unused.
- Configure antivirus.
- Manage updates carefully (the lecture says "disable auto-updates"; in practice this is debated, the point is to **control** when patches apply).
- Set up backups.
- Enforce strong authentication; admin/root passwords.

### General hardening definition
> Making an OS more secure by configuring system + network properly, patching, removing unnecessary files/software, protecting BIOS with a password, disabling unused bootable devices.

Hardening shrinks the **attack surface**: fewer features exposed, fewer apps installed = less to exploit.

## 7. Linux hardening with Harbian ([[linux-hardening]])

### Why Linux security matters
Many widely-used services and devices run Linux (servers, Android, embedded, web apps). Non-technical users share private data with them constantly via apps and web services. Hardening Linux is a real concern, not a niche one.

### Harbian
A Debian-based distribution **specifically aimed at hardening**. Provides tools (in their GitHub repo) including a hardening **audit script**.

### Running the audit (case study)
The lecturer ran `hardening.sh --audit-all` inside a Docker container (safe sandboxing for unfamiliar scripts).
- Ran ~272 static tests.
- ~97 passed, ~172 "failed".

Important nuance: not every failure means insecurity. The script tests "if web server is installed, is it configured right?". If no web server is installed, the test "fails", but that's arguably safer.

### What the script checks
- File permissions.
- User-account configuration (e.g. no users in the `shadow` group).
- `.rhosts` files in home directories (DNS-reconfig vector).
- **SUID binaries** (programs running with elevated privileges, attack vector if compromised).
- ... and ~260 more.

### Takeaway
For non-experts, this kind of community-maintained audit script is a much richer guide than a generic blog-post checklist. The repo is updated as new exploits surface, so the test set tracks current best practice.

## Common pitfalls / exam fodder
- Mixing up **OSI** and **TCP/IP** layer counts (7 vs 4) and which layer does what.
- Calling **IDS** and **IPS** the same thing. IDS = camera; IPS = guard.
- Forgetting **stateful vs stateless** firewall trade-offs.
- Saying "DAC is the most secure" because it gives users control, it's the opposite, DAC has **low** security.
- Treating hardening as a one-off, it's continuous (patches, audits, new exploits).
- Assuming "no failures" in an audit = secure. Context matters: some "failures" are absences of optional software.

## Related concepts (KB stubs)
- [[osi-tcp-ip-models]], [[tcp]], [[http]], [[ip]]
- [[firewall]] (stateless, stateful, proxy)
- [[ids]], [[ips]], [[ngfw]]
- [[access-control-models]], [[least-privilege]], [[rbac]], [[abac]]
- [[os-hardening]], [[linux-hardening]]
- [[attack-surface]]
- [[cia-triad]] (confidentiality / integrity / availability)
