
---

#  Purple Team Outcome Report

**Lab 5 — Threat Hunting & Purple Team Operations**

**Objective:**
Demonstrate how proactive threat hunting directly improves detection coverage, alert fidelity, and SOC response effectiveness.

This report documents how findings from **Labs 3 & 4** were operationalized into **new detections and improved alert logic** through structured threat hunting.

---

##  1. Hunt Inputs (Red / Threat-Informed Signals)

### Source Telemetry

* SSH authentication logs (Linux)
* Detection alerts from:

  * Lab 3: SSH Brute Force Detection
  * Lab 4: DNS Beaconing (C2 patterns)

### Adversary Techniques Observed

| Source                     | Technique         | MITRE ID  |
| -------------------------- | ----------------- | --------- |
| SSH Brute Force            | Credential Access | T1110     |
| SSH Success After Failures | Initial Access    | T1078     |
| DNS Beaconing              | Command & Control | T1071.004 |

---

##  2. Threat Hunting Hypothesis (Executed)

> **Hypothesis:**
> Adversaries who gain SSH access via brute-force will exhibit post-compromise behaviors distinguishable from legitimate admin activity.

### Indicators Tested:

* Multiple failed SSH attempts followed by success
* Login outside business hours
* Access from external IP ranges
* Privileged account usage (root)

---

##  3. Detection Gaps Identified (Before Hunt)

| Gap                                           | Impact                             |
| --------------------------------------------- | ---------------------------------- |
| Brute-force detection ended at initial access | No visibility into post-compromise |
| No correlation between failures + success     | Alert fatigue, missed compromise   |
| No privilege-aware logic                      | Root compromise not escalated      |

---

##  4. Purple Team Improvements Implemented

###  New Detection Added

**Detection Name:** `SSH Post-Compromise Activity`

**Logic Enhancements:**

* Correlates:

  * ≥5 failed attempts
  * Successful login from same IP
* Elevates severity if:

  * Account = `root`
  * Time = non-business hours
* Outputs analyst-ready alert context

**Resulting Alert:**

```
ALERT: Post-compromise SSH activity detected
IP=185.234.218.11
Failures=6
SuccessTime=2025-01-10 02:14:27
```

---

##  5. Measurable Blue Team Impact

| Area                       | Improvement                                |
| -------------------------- | ------------------------------------------ |
| Detection Fidelity         | Reduced false positives                    |
| Mean Time to Detect (MTTD) | Improved via correlation                   |
| Analyst Confidence         | Clear compromise narrative                 |
| Coverage                   | Extended from Initial Access → Persistence |

 **Executive Translation:**
I moved from detecting *attempts* to detecting *actual compromise*.

---

##  6. Feedback Loop (Purple Team Cycle)

1. Threat Hunting exposed behavioral gap
2. Detection logic enhanced
3. Alerts became context-rich
4. SOC response faster and more accurate

This is the **Purple Team flywheel** in action.

---

##  7. Final Outcome

✔️ Threat hunting informed detection engineering
✔️ Detection coverage expanded across kill chain
✔️ SOC alert quality materially improved
✔️ Blue Team posture hardened against real adversaries

---

##  Why This Matters to Employers

This lab demonstrates ability to:

* Hunt like an attacker
* Engineer like a defender
* Communicate like a leader

This is **Tier 3 SOC / Detection Engineering / Purple Team capability**.

---
