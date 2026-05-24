# Topic 1: Identification and Classification of Cyber Threats

> CM2025 · Weeks 1-2, Topic 1 · 3 lectures
> Source transcripts: `notes/transcripts/01-identification-and-classification-of-cyber-threats/` (local, gitignored)

## TL;DR
A **cyber threat** is any attempt to gain unauthorised access to a system, network, or device to cause harm. Threats are classified along three axes: **origin** (insider vs external), **vector** (network vs endpoint), and **impact** (financial vs reputational). **Cyber Threat Intelligence (CTI)** turns raw data about attackers into actionable defence by working at four levels (strategic, tactical, operational, technical) and feeds into layered mitigation strategies (defence in depth).

## What is a cyber threat? ([[cyber-threat]])

> Any attempt to gain unauthorised access to a system, network, or digital device with intent to cause harm.

### Common threat types

| Threat | What it does | Quick example |
|---|---|---|
| **Malware** | Malicious software, steals data / spies / destroys files | Viruses, trojans |
| **Phishing** | Tricks users into giving up credentials via fake-legit comms | Bank-impersonation email |
| **Ransomware** | Encrypts files, demands payment for decryption key | WannaCry (2017) |
| **Social engineering** | Psychological manipulation, not technical | Pretending to be tech support |
| **Information manipulation/interference** | Spreading false or altered data to confuse, influence decisions | Election interference |
| **Supply chain attack** | Compromise a less-secure third party to reach the real target | SolarWinds (2020) |

### Real-world cases worth knowing
- **WannaCry (2017)**, ransomware infected 200,000+ machines in 150+ countries; hit NHS hospitals (UK), surgeries cancelled. Demanded Bitcoin. Billions in damage.
- **Equifax breach (2017)**, personal data of ~150 million people stolen via an unpatched vulnerability.
- **SolarWinds (2020)**, malware injected into a legitimate software update, pushed to thousands of customers including major government agencies; undetected for months.

## Classifying cyber threats ([[threat-classification]])

A three-axis model: **who** (origin), **how/where** (vector), **what** (impact).

### Axis 1, Origin: insider vs external

| Type | Description | Sub-types | Example |
|---|---|---|---|
| **Insider** | Comes from within the organisation, current/former staff, contractors, partners with access | Malicious (deliberate) vs Negligent (accidental, e.g. lost device, phishing fall) | Tesla 2020, staff offered money to install malware (reported it) |
| **External** | Comes from outside | Cybercriminals, hacker groups, state-sponsored actors, hacktivists | WannaCry vs NHS (2017) |

### Axis 2, Vector: network vs endpoint

| Vector | Targets | Example attacks |
|---|---|---|
| **Network-based** | Servers, routers, cloud infra | DDoS, man-in-the-middle, port scanning |
| **Endpoint** | User devices (laptops, phones, tablets) | Phishing email, keylogger, ransomware on a workstation |

Endpoint attacks can be the entry point for much larger network-wide intrusions.

### Axis 3, Impact: financial vs reputational

| Impact | Nature | Example |
|---|---|---|
| **Financial** | Immediate (ransom, downtime) or long-term (legal, recovery) | Colonial Pipeline (2021): ~$3.5m ransom + disruption losses |
| **Reputational** | Loss of trust; can outlast the incident itself | Sony Pictures hack (2014): leaked emails + unreleased films |

> Exam-style reflection: which is harder to recover from, lost money or lost trust?

## Cyber Threat Intelligence (CTI) ([[cyber-threat-intelligence]])

> The process of collecting and analysing data to understand potential or active threats, so the organisation can **predict** attacks, not just react.

CTI captures four things about a threat:
- **Who** the attacker is
- **Why** they are attacking
- **How** they execute
- **What indicators** to look for to detect early

### Four levels of CTI

| Level | Audience | Content | Time horizon |
|---|---|---|---|
| **Strategic** | Senior leadership | Broad trends, emerging risks | Long-term planning |
| **Tactical** | Security analysts | Attacker tools, techniques, procedures (TTPs) | Medium-term |
| **Operational** | SOC, incident responders | Real-time campaign insight | Immediate defence adjustments |
| **Technical** | Tooling / blocklists | Malware hashes, malicious IPs, phishing domains | Short-term, blocking |

### Intelligence sources

| Internal | External |
|---|---|
| System logs | Government advisories (NCSC in UK, CISA in US) |
| Incident reports | OSINT (open-source platforms, forums) |
| User activity logs | ISACs (sector-specific sharing groups) |
| | Commercial intelligence feeds |

Best practice: combine multiple sources for a fuller picture.

### CTI lifecycle (continuous)

```
1. Collect data from trusted sources
2. Analyse  relevance + accuracy
3. Correlate with own environment
4. Act     block domains, update firewalls, alert
5. Review  refine defences; loop
```

## Mitigation strategies (defence in depth)

No single control is enough; build **layers**. Outer to inner:
1. **MFA** to block unauthorised access.
2. **Endpoint protection + firewalls** to shrink the attack surface.
3. **Staff awareness training** to resist social engineering.
4. **Regular patching + updates** to close known vulnerabilities.
5. **Tested, secure backups**.
6. **Continuous network monitoring + alerting** for suspicious activity.

### Worked example: ransomware defence
- Block phishing emails (filters + training) before the user sees them.
- **Least privilege**, attackers who land can't move laterally.
- **Off-site backups** done regularly.
- **Tested incident response plan**.
- **Monitoring tools** to detect lateral movement.

Each adds resilience; together they reduce the chance of full compromise.

## Common pitfalls / exam fodder
- Treating cybersecurity as "a tech problem" only, it's people + process + tech.
- Assuming a perfectly secure system is achievable, it isn't; assume breach and prepare to detect/respond.
- Buying one product (e.g. just antivirus) and calling it done. Need **layered** defence.
- Confusing CTI with raw logs. Intelligence is data turned into **actionable knowledge**.

## Related concepts (KB stubs)
- [[cyber-threat]], [[threat-classification]], [[cyber-threat-intelligence]]
- [[ransomware]], [[phishing]], [[social-engineering]], [[supply-chain-attack]]
- [[defence-in-depth]]
- [[ddos]], [[man-in-the-middle]]
- [[least-privilege]]
- [[incident-response-plan]]
