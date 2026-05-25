# Topic 4: Application Security Principles, Testing and Debugging

> CM2025 · Weeks 7-8, Topic 4 · 4 lectures
> Source transcripts: `notes/transcripts/04-application-security-principles-testing-and-debugging/` (local, gitignored)

## TL;DR
**Application security (AppSec)** = making applications resistant to threats across their entire lifecycle. The exam-relevant pillars: a small set of **secure coding principles** (least privilege, input validation, secure defaults, defence in depth, fail securely), **OWASP Top 10** as the canonical risk catalogue, and two testing approaches you must distinguish: **DAST** (run-time, black/grey-box, OWASP ZAP-style) vs **SAST** (source-code static analysis). Secure file handling is the lecture's chosen worked example, and it maps directly to the [[cia-triad]].

## 1. What is AppSec? ([[appsec]])

> Practice of making applications **resistant to threats** through tools, processes, and best practices across **design, development, and maintenance**.

Applies to web, mobile, desktop, and cloud apps. Has to live throughout the **software lifecycle**, not bolted on at the end.

### Why it matters
Vulnerable apps cause data leaks, account compromise, system breaches, financial loss, reputation damage, legal penalties. The lecture's claim: **most of these issues are avoidable** with the right practices.

### Core security principles (recur across all 4 lectures)

| Principle | What it means | Practitioner translation |
|---|---|---|
| **Least privilege** ([[least-privilege]]) | Give users / components only the access they need | The thing you've been doing with `setcap`, `sudo`, dedicated service users for 15 years |
| **Input validation** | Never trust external input; check + clean | Sanitise at the boundary, parameterised queries, whitelist-based validation |
| **Secure defaults** | Systems must be secure **out of the box**, not after admin tweaks | A criticism Windows gets a lot in CM2025; UNIX too, sometimes |
| **Defence in depth** ([[defence-in-depth]]) | Layer multiple controls, don't rely on one | Already covered in Topic 1 mitigation |
| **Fail securely** | When something breaks, fail closed, not open | E.g. auth error path defaults to deny, not allow |
| *(secure coding adds)* **Avoid security through obscurity** | Hiding flaws ≠ fixing them | Old chestnut, no surprise |
| *(secure coding adds)* **Keep it simple** | Simpler code = fewer places for bugs to hide | KISS principle |
| *(secure coding adds)* **Output encoding** | Encode output (HTML/JS/URL) to stop injection on display | Prevents stored XSS reaching the browser |

### OWASP Top 10 ([[owasp-top-10]])

**OWASP** = Open Worldwide Application Security Project. Non-profit, free resources.

The OWASP Top 10 (2021 edition cited in lecture) = canonical list of the most common, critical risks in web apps. Lecture only enumerates the first five but the exam-quotable phrasing matters:

1. **Broken access control**
2. **Cryptographic failures**
3. **Injection** (SQL, command, LDAP, etc.)
4. **Insecure design**
5. **Security misconfiguration**
6. Vulnerable + outdated components
7. Identification + authentication failures
8. Software + data integrity failures
9. Security logging + monitoring failures
10. Server-side request forgery (SSRF)

> The lecture only lists 1-5 explicitly. The full 2021 list is included above for completeness.

### Who's responsible for AppSec?

> "It's everyone's job."

| Role | Responsibility |
|---|---|
| **Developers** | Write secure code |
| **Architects** | Design secure systems |
| **DevOps** | Maintain secure environments |
| **Security teams** | Guide + monitor |
| **Users** | Follow practices (passwords, MFA, etc.) |

## 2. Secure coding ([[secure-coding]])

### Why insecure code happens
- Shortcuts (deadline pressure)
- Copy-paste from Stack Overflow / forums without review
- Outdated libraries (no scanning, no SCA)
- Skipped input validation
- No training in secure coding

### Real-world breach causes the lecture cites
- **Hard-coded admin password** in social-media platform breach
- Healthcare app exposing **patient data**
- Online shop **card-data theft**
- Government site **downtime from unhandled errors**

### Secure coding best-practice checklist
- Clean **all** input
- Use **parameterised queries** for DB access (never string-concat SQL)
- Implement **proper authentication** (no rolling your own crypto, no homebrew session tokens)
- **Never hard-code passwords / secrets** (use env vars, secrets managers, vaults)
- Use **well-maintained libraries** (regular SCA scans, dependency updates)
- Write **proper error messages** (informative for the user, **non-revealing** for the attacker, e.g. don't leak stack traces)
- **Code review with security in mind** (not just functional review)

### Lifecycle integration
| Stage | Security activity |
|---|---|
| **Requirements + design** | Define security goals, threat-model, secure architecture |
| **Development** | Follow secure-coding practices |
| **Testing** | Include security tests (DAST/SAST/dependency scans) |
| **Deployment** | Lock down configurations |
| **Post-launch** | Patch, monitor, respond to new CVEs |

> Security is continuous, not a one-shot pre-release gate.

## 3. Secure file handling ([[secure-file-handling]])

The lecture's worked example. Maps directly onto the **[[cia-triad]]** (confidentiality, integrity, availability).

> Secure file handling = safe and responsible management of files across the **upload / download / access / store / delete** lifecycle.

### Why files are dangerous
Files often carry:
- Personal data
- Credentials
- System configuration

If attackers get to those files or exploit weak handling, they introduce **malware**, **steal data**, or **disable systems**.

### Risk types if file handling is sloppy
| Risk | Concrete example |
|---|---|
| Unauthorised file access | Attacker reads `/etc/passwd` via path traversal |
| Malware upload | User uploads `evil.php` disguised as `image.jpg`; server executes it |
| Data exfiltration via exposed directories | Listable `/uploads/` directory with sensitive PDFs |

### Defence layers

| Layer | What to do |
|---|---|
| **Validation** | Check **actual content type**, not just the extension. Whitelist allowed types. Apply **size limits** (DoS prevention). |
| **Sanitisation** | Strip dangerous chars from filenames (`/`, `..`, etc., the **path traversal** vectors). Save with **server-generated names**. Strip embedded macros/scripts. |
| **Access control** | Apply [[least-privilege]] on file perms. Files **not** globally read/write unless required. Uploaded files in a directory that **doesn't allow execution** or public access. |
| **Secure storage** | Encrypt sensitive files at rest. Never store passwords/tokens **plaintext**. Use encrypted archives or DB-level encryption. |
| **Upload safety** | Treat all uploads as **untrusted until proven safe**. Don't store in web-accessible folders. Scan with AV. Rename server-side. Validate **both client and server side** (client side for UX, server side for security). |
| **Monitoring** | Log uploads/downloads/deletes; track per-user activity; alert on anomalies (one user downloading thousands of files); run **file-integrity checks** on critical assets. |

### Practitioner note (your Linux background)
This is basically the same playbook as hardening any UNIX file-serving box: restrictive umask, noexec mounts for upload dirs, AppArmor/SELinux profiles, server-side filename generation, ClamAV scanning. The exam wording leans more on "validate, sanitise, store securely" categories than the Linux-specific knobs, so reach for the **categories** in the exam answer.

## 4. Dynamic Application Security Testing (DAST) ([[dast]])

> A method of testing applications **while they are running**, by interacting with them from the outside the way an attacker would.

### How DAST works (worked example)
1. Run the app in a test environment.
2. Run a DAST scanner (e.g. **OWASP ZAP**, **Burp Suite**) against it.
3. Scanner injects suspicious input into forms / endpoints:
   - SQL injection probes: `' OR 1=1 --`, `admin' --`
   - XSS probes: `<script>alert('XSS')</script>`
4. Scanner watches for unusual responses, errors, redirects, exposed data.
5. Scanner reports findings; dev team fixes before release.

> Topic 4's ungradedLab was the OWASP ZAP one (id `Mb4IB`), this is exactly the tool being demonstrated.

### DAST vs SAST ([[dast-vs-sast]])

| Aspect | **DAST** | **SAST** |
|---|---|---|
| When | Application is **running** | Static, source code only |
| Code access | **Not required** | **Required** |
| Perspective | **External** (attacker's view) | **Internal** (developer's view) |
| What it catches | Runtime behaviour: misconfigs, broken auth, response leaks | Code logic: insecure functions, taint flow, dangerous APIs |
| Language-dependent? | No, works across stacks | Yes, parser per language |
| Misses | Internal logic bugs, dead code | Things that only emerge at runtime |

> Best practice: **use both** (plus dependency scanning / SCA). They cover different failure modes.

### Black-box vs grey-box testing

| Approach | Knowledge of system | Use case |
|---|---|---|
| **Black-box** | None, tester is just like an external attacker | Pure attacker simulation, pen-testing, late-stage assurance |
| **Grey-box** | Partial: tech stack, user roles, architecture | Faster + more targeted testing in DevSecOps flows |
| (White-box, for context) | Full source + design access | Code review, threat modelling |

DAST naturally fits **black-box** and **grey-box**.

### DAST advantages
- Finds **runtime-only** vulnerabilities.
- **Language-independent**, works across platforms.
- No source-code access needed (great for third-party / vendor apps).
- Helps **compliance** (validates runtime behaviour).
- Suits black-box + grey-box testing.

### DAST limitations
- Misses **internal logic flaws** (SAST catches these).
- Needs a **running app**, not usable in early dev.
- **False positives** are common (tool can't always tell exploit from quirk).
- Incomplete coverage if scanner can't reach all app paths (e.g. requires auth or specific session state).
- **Best combined** with SAST + SCA + manual review.

### Common DAST tools

| Tool | Notes |
|---|---|
| **OWASP ZAP** | Free, open source, beginner-friendly. The course's lab tool. |
| **Burp Suite** | Powerful, pen-tester favourite (free + paid editions) |
| **Acunetix** | Enterprise |
| **Netsparker** | Enterprise |
| **IBM AppScan** | Large-scale teams |
| **Coalesce Web Application Scanner** | Large-scale teams |

## Common pitfalls / exam fodder
- **OWASP Top 10**: be able to recall **at least the top 5** (broken access control, cryptographic failures, injection, insecure design, security misconfiguration). The full list is good to know but the first 5 is what the lecture explicitly enumerates.
- **DAST vs SAST** confusion: black-box vs white-box, runtime vs source, internal vs external. The table above is the exam-killer.
- "Black-box" doesn't mean "no understanding", it means "no access to source/internals". Grey-box adds partial knowledge.
- **Validate file content type, not just file extension** is a likely quiz target (it was emphasised in the lecture).
- "Security through obscurity" is not security, even though it's a recurring real-world temptation.
- **OWASP ZAP** is the canonical example tool for DAST in this course (and what the lab uses).

## Practitioner notes (your Linux background)
- Most of this is what you've been doing on production Linux for years: least privilege, parameterised SQL, no plaintext secrets, no world-writable file perms, ClamAV/AV on uploads, audit logging.
- The exam framing leans more on **OWASP categories** + **DAST/SAST terminology** than on the specific knobs you'd actually turn in production.
- When in doubt, give the textbook category name (e.g. "broken access control") rather than the practitioner technique (e.g. "we use IAM policies + RBAC + per-resource policies"), the marker is looking for the OWASP-style vocabulary.

## Related concepts (KB stubs)
- [[appsec]], [[owasp-top-10]], [[owasp-zap]]
- [[secure-coding]], [[secure-file-handling]]
- [[dast]], [[sast]], [[sca]] (software composition analysis)
- [[input-validation]], [[output-encoding]], [[sanitisation]]
- [[path-traversal]], [[sql-injection]], [[xss]]
- [[cia-triad]] (already linked from Topic 3 / OS hardening)
- [[least-privilege]], [[defence-in-depth]] (recur from Topic 1)
- [[devsecops]]
