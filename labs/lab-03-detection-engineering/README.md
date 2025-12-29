---

# Lab 3: SSH Brute-Force Detection Engineering & SOC Investigation

## Overview

This lab simulates a real-world SOC detection engineering workflow by identifying, alerting on, and investigating an SSH brute-force attack that results in a successful compromise.

The objective is to demonstrate how raw authentication logs are transformed into:
- High-fidelity detections
- Actionable alerts
- Analyst-ready investigation context
- MITRE ATT&CK–aligned intelligence

This mirrors how modern SOCs, MDR providers, and threat hunting teams operate.

---

## Threat Scenario

An external attacker performs repeated SSH login attempts against common and privileged accounts (`admin`, `root`). After multiple failures, the attacker successfully authenticates as `root`, indicating a completed credential compromise.

This scenario represents a **confirmed intrusion**, not a benign anomaly.

---

## Detection Logic

A custom Python detection was developed to:

- Parse SSH authentication logs
- Track failed login attempts by source IP
- Detect a threshold-based brute-force pattern
- Correlate failures with a subsequent successful login
- Generate a high-confidence alert

### Alert Generated

```

ALERT: SSH brute-force compromise detected
Source IP: 185.234.218.11
Failed Attempts: 6
Compromise Time: 2025-01-10 02:14:27

```

This logic intentionally focuses on **signal over noise**, reducing false positives common in basic brute-force alerts.

---

## SOC Analyst Investigation

Following alert generation, an analyst investigation was performed to validate the incident, assess impact, and determine escalation priority.

Analyst actions included:
- Confirming attack timeline and source IP
- Identifying compromised account (`root`)
- Distinguishing malicious activity from normal administrative access
- Assessing privilege level and potential blast radius

Detailed investigation notes are documented in:

```

analysis/investigation_notes.md

```

---

## MITRE ATT&CK Mapping

The detection and investigation align with the following adversary techniques:

- **T1110 – Brute Force** (Credential Access)
- **T1078 – Valid Accounts** (Initial Access / Persistence)

This represents a complete attack path from credential abuse to privileged access.

Full mapping is documented in:

```

analysis/mitre_mapping.md

```

---

## Business & Security Impact

- Root-level access enables full system compromise
- Potential for lateral movement and data exfiltration
- Requires immediate containment and credential rotation
- High risk due to attacker success, not just attempts

This alert would warrant **urgent escalation** in a production SOC environment.

---

## Evidence Artifacts

This lab includes reproducible artifacts suitable for audit and peer review:

```

logs/ssh_auth.log                  → Raw authentication data
detections/ssh_bruteforce_detection.py → Detection logic
analysis/investigation_notes.md    → Analyst reasoning
analysis/mitre_mapping.md          → ATT&CK alignment

```

---

## Skills Demonstrated

- Detection engineering (Python)
- Log parsing and correlation
- SOC alert triage and investigation
- MITRE ATT&CK mapping
- Incident severity assessment
- Git-based security workflow

---

## Why This Matters to Employers

This lab demonstrates the ability to:
- Build detections, not just tune tools
- Identify attacker success, not just activity
- Think like a SOC analyst under pressure
- Communicate incidents clearly and defensibly

This is the same workflow used by enterprise SOCs, MDR teams, and threat hunting groups.

---

## Status

**Lab 3: Complete – Detection Validated, Investigated, and Documented**
```

---

## My Final Confirmation

I now have:

✔ Detection logic
✔ Alert generation
✔ SOC investigation narrative
✔ MITRE ATT&CK mapping
✔ Recruiter-readable story

This is **not junior content**. This is exactly what hiring managers mean when they say *“show me how you think.”*

---
