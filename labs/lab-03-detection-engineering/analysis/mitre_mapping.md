---

## 🎯 Objective (Phase B – MITRE Mapping)

I Created a **formal MITRE ATT&CK mapping artifact** that:

* Ties my SSH brute-force detection to adversary behavior
* Shows that I understand **attack progression**, not just alerts
* Matches how real SOCs document detections

This will live in my repo and be referenced by the README.

---

# MITRE ATT&CK Mapping

**Lab 3 — SSH Brute-Force Detection & Compromise Identification**

## Detection Overview

This detection identifies SSH brute-force activity resulting in successful authentication. It correlates repeated failed login attempts from a single source IP with a subsequent successful login to a privileged account.

The behavior reflects adversary techniques used to gain unauthorized access through credential abuse.

---

## Primary MITRE ATT&CK Techniques

### 🔴 T1110 — Brute Force

**Tactic:** Credential Access

**Why this applies:**
The attacker repeatedly attempted SSH authentication using common and privileged usernames (`admin`, `root`) from a single external IP address in a short time window.

**Observed Evidence:**

* Multiple failed SSH login attempts
* Username enumeration
* High-frequency authentication failures

**Log Indicators:**

```
Failed password for invalid user admin
Failed password for invalid user root
```

---

### 🔴 T1078 — Valid Accounts

**Tactic:** Initial Access / Persistence

**Why this applies:**
After repeated failures, the attacker successfully authenticated using the `root` account, indicating the use of valid credentials obtained through brute-force guessing.

**Observed Evidence:**

* Successful SSH login following failed attempts
* Privileged account access (`root`)

**Log Indicator:**

```
Accepted password for root from 185.234.218.11
```

---

## Adversary Kill Chain Progression

| Phase                | Technique              | Evidence                   |
| -------------------- | ---------------------- | -------------------------- |
| Credential Access    | T1110 – Brute Force    | Repeated failed SSH logins |
| Initial Access       | T1078 – Valid Accounts | Successful root login      |
| Privilege Escalation | Inherent               | Root-level access obtained |

This progression demonstrates a **completed attack path**, not just reconnaissance or noise.

---

## Detection Value

* High-fidelity alert (low false positive risk)
* Captures attacker success, not just attempts
* Enables rapid containment before lateral movement
* Aligns with real-world SOC and MDR detection logic

---

## Coverage Gaps & Future Enhancements

Potential enhancements to expand coverage:

* Detect SSH key abuse (T1098)
* Correlate with post-authentication commands (T1059)
* Add geo-anomaly enrichment for source IPs
* Integrate with automated response actions

---

## Analyst Assessment

This detection effectively identifies **credential-based intrusions** and provides strong visibility into adversary behavior aligned with the MITRE ATT&CK framework. It supports rapid incident escalation and incident response workflows.

---

##  What This Proves

That I’ve now shown I can:

* Translate logs into adversary techniques
* Map detections to ATT&CK **correctly**
* Explain *why* a detection exists
* Think like a detection engineer, not a tool user

This is **mid-level SOC / detection engineer territory**.

---

