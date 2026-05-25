# Static Application Security Testing (SAST), Crowdstrike

> **Citation:** Gale, J. (2025). *Static Application Security Testing (SAST) explained*. CrowdStrike.
> **URL:** https://www.crowdstrike.com/en-gb/cybersecurity-101/cloud-security/static-application-security-testing-sast/
> **Used by CM2025 Topic 4, Lesson 3 supplement: "Application security testing technique"**

## Lecturer's framing questions
- Why is it valuable to identify security flaws **during the coding stage** rather than after deployment?
- What potential challenges might developers face when relying on SAST tools (accuracy, integration)?

## Summary

### What SAST is
Automated approach that **scans source code for vulnerabilities before deployment**. Identifies security flaws, code quality issues, and compliance violations **without running the application**.

### How it works
Integrates with Git, IDEs, and CI/CD pipelines for real-time feedback. Static analysis examines code without executing it, scanning the codebase including dependencies and configuration files.

Three analysis techniques:
- **Lexical analysis**: structural and formatting errors (unrecognised tokens, improper keywords)
- **Semantic analysis**: logic flaws like buffer overflows
- **Pattern matching**: hard-coded credentials, known-vulnerable dependencies

### Vulnerabilities SAST detects
- Buffer overflows, insecure deserialisation
- XSS, SQL injection, input-sanitisation flaws
- Hard-coded credentials, vulnerable dependencies
- Code quality issues (improper error handling, dead code, resource leaks)

### Key benefits
- **Early detection** ("shift-left" security)
- Fast and cost-effective vs runtime testing
- Real-time feedback in developer workflow
- Comprehensive code-level coverage

### SAST vs DAST (Crowdstrike's framing)

| Aspect | SAST | DAST |
|---|---|---|
| Execution | No runtime needed | Tests during runtime |
| Code access | Analyses source directly | No source access |
| Method | Static analysis | Simulated attacks |
| Timing | Early in development | Later, closer to deployment |

The two are **complementary** and should work together across the SDLC.

### Limitations
- **False positives**, manual triage needed
- **Complex issues** need specialist input to root-cause
- **Limited runtime visibility** (misses race conditions, env-specific misconfigs)
- **Dependency gaps**, struggles with open-source dependencies; supplement with **SCA** tools

### Recommended approach
> "SAST should be used alongside SCA, DAST, and ASPM to provide comprehensive security coverage."

Multi-layered: SAST + SCA (Software Composition Analysis) + DAST + ASPM (Application Security Posture Management).
