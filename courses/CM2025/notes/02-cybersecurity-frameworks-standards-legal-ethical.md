# Topic 2: Cybersecurity Frameworks, Standards, Legal, Ethical, and Professional Considerations

> CM2025 · Weeks 3-4, Topic 2 · 2 lectures
> Source transcripts: `notes/transcripts/02-cybersecurity-frameworks-standards-legal-ethical-and-professional-considerations/` (local, gitignored)

## TL;DR
Strong technical defences are useless without governance, planned risk, and legal compliance. **GRC** (Governance, Risk Management, Compliance) bundles those three responsibilities together. Two related but distinct tools support GRC in practice: **standards** (external best-practice frameworks, e.g. ISO 27001, NIST CSF) and **policies** (internal rules that tell staff how to behave). Standards guide structure; policies control behaviour.

## GRC: Governance, Risk, Compliance ([[grc]])

| Component | What it is | Role |
|---|---|---|
| **Governance** | How the organisation is directed and controlled, leadership, accountability, policy | Sets the direction |
| **Risk management** | Identifying and reducing potential threats | Protects what matters most |
| **Compliance** | Meeting legal, regulatory, contractual obligations (GDPR, ISO, etc.) | Keeps everything within the law |

Together GRC aligns security decisions with business goals and legal duties.

### Governance ([[governance]])
Makes cybersecurity a **business priority**, not just a tech problem.
- Aligns security strategy with org-wide goals.
- Defines who is responsible for what decisions and actions.
- Sets policies for acceptable use, data protection, response.
- Promotes transparency, ethics, accountability.

Without it: security becomes disorganised, reactive, or itself risky.

### Risk management ([[risk-management]])
**Proactive**, not reactive. A continuous loop:
1. **Identify** threats (system vulnerabilities, human error, supply chain).
2. **Assess** likelihood and impact.
3. **Treat**: mitigate (add controls, training, redesign), or **accept** if low/manageable.
4. **Monitor** continuously.

Focuses resources on the most serious threats.

### Compliance ([[compliance]])
Meeting the rules, whether law, regulator, industry body, or internal policy.

Examples:
- **GDPR** (EU), personal-data handling.
- **NIST**, **ISO** standards for critical infrastructure.
- **PCI DSS** for organisations handling card data.

Why it matters: avoids fines, lawsuits, reputational harm; builds trust with customers and partners.

### GRC in practice (worked example: healthcare provider)
| GRC component | What it looks like |
|---|---|
| Governance | Appoint a **CISO** to lead security strategy |
| Risk management | Assess impact if patient data leaked |
| Compliance | Follow GDPR + NHS cybersecurity standards |

## Standards vs policies

The exam-friendly distinction:

|  | **Standards** | **Policies** |
|---|---|---|
| Origin | External (formal bodies: ISO, NIST, BSI) | Internal (org's own) |
| Nature | Best-practice frameworks | Operational rules and procedures |
| Audience | Used by orgs to benchmark / show compliance | Staff: how they must behave |
| Force | Often **voluntary**, but widely adopted | Enforceable internally |
| Purpose | Guide the **structure** | Control the **behaviour** |

> "Standards guide the structure, policies control the behaviour."

### Major cybersecurity standards ([[cybersecurity-standards]])

| Standard | Issuer | Scope |
|---|---|---|
| **ISO/IEC 27001** | ISO | Establishing an Information Security Management System (ISMS) |
| **NIST CSF** | NIST (US) | Identify, Protect, Detect, Respond, Recover, the 5 core functions |
| **PCI DSS** | PCI Council | Mandatory for any org handling credit/debit card data |
| **GDPR** | EU | Legal regulation (not strictly a security standard) with strict data-protection/security requirements |

### Common cybersecurity policies ([[cybersecurity-policy]])

| Policy | Purpose |
|---|---|
| **Acceptable Use Policy (AUP)** | What staff can/can't do on company systems |
| **Access Control Policy** | How access to systems/data is granted (see [[access-control-models]]) |
| **Data Classification Policy** | How data is labelled by sensitivity |
| **Incident Response Policy** | What to do if a breach occurs |
| **BYOD Policy** | Rules for personal devices used for work |
| **Password Policy** | Strong-authentication requirements |

Good policies are clear, enforceable, regularly updated, and reflect current standards + legal obligations.

## Why standards + policies matter
- Create structure for defending data.
- Define responsibility.
- Reduce risk of errors, insider threats, legal trouble.
- Increase trust across the business.
- Show regulators + customers the org takes security seriously.

## Common pitfalls / exam fodder
- Mixing up **standards** with **policies**: standards are external, voluntary frameworks; policies are internal enforceable rules.
- Listing GDPR as a "cybersecurity standard", it's a **legal regulation** with security requirements baked in.
- Thinking "compliance" = "secure". Compliance is a baseline, not a ceiling.
- Confusing the three Rs in NIST CSF (Identify, Protect, **Detect, Respond, Recover**).

## Related concepts (KB stubs)
- [[grc]], [[governance]], [[risk-management]], [[compliance]]
- [[cybersecurity-standards]], [[cybersecurity-policy]]
- [[iso-27001]], [[nist-csf]], [[pci-dss]], [[gdpr]]
- [[isms]] (Information Security Management System)
- [[ciso]] (TODO)
