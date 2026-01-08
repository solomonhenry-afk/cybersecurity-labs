---

##  Lab 6 — Cloud GRC Mapping (NIST · CIS · CSA CCM)

###  Why This Lab Exists (Recruiter Context)

Most cloud security portfolios stop at **detections**.

This lab proves I can go further — translating **technical cloud risk** into **governance, risk, and compliance (GRC)** language that executives, auditors, and regulators understand.

This is how real organizations:

* Pass audits
* Justify security investment
* Reduce breach impact **before incidents occur**

---

##  Lab Objective

Design a **cloud security control mapping framework** that connects:

* Cloud-native misconfigurations (Azure, Kubernetes, CNAPP findings)
* To **recognized compliance frameworks**
* With **clear executive accountability and remediation ownership**

This mirrors how security leaders operationalize:

* NIST RMF
* CIS Critical Security Controls
* CSA Cloud Controls Matrix (CCM)

---

##  What I Built

### 🔹 1. Control-to-Cloud Mapping (Technical → Governance)

Mapped real cloud risks from earlier labs to:

* **NIST SP 800-53**
* **CIS Controls v8**
* **CSA CCM**

Each mapping includes:

* Control ID
* Cloud service affected (Azure, AKS, Storage, IAM)
* Risk description
* Expected control outcome

 Stored in:

```
controls/
```

---

### 🔹 2. Risk Analysis Narrative (Executive-Readable)

Created analyst-grade explanations that answer:

* *Why does this cloud risk matter to the business?*
* *What happens if this control fails?*
* *Who owns remediation?*

 Stored in:

```
analysis/
```

This demonstrates the ability to brief:

* CISOs
* Risk committees
* Audit stakeholders

---

### 🔹 3. Evidence & Audit Readiness

Designed artifacts that could be handed directly to:

* Internal audit
* External assessors
* Cloud governance teams

 Stored in:

```
evidence/
```

---

##  How This Connects to Earlier Labs

| Prior Lab         | What It Showed                     | How Lab 6 Elevates It                            |
| ----------------- | ---------------------------------- | ------------------------------------------------ |
| IaC Security      | Misconfigured cloud infrastructure | Mapped to CIS + NIST preventive controls         |
| IAM Misconfig     | Identity attack paths              | Mapped to access control & least privilege       |
| Kubernetes        | Baseline & runtime risk            | Mapped to workload protection standards          |
| CNAPP Correlation | Attack paths                       | Mapped to governance oversight & risk acceptance |

This closes the loop from **technical signal → executive decision**.

---

##  Real-World Roles This Demonstrates Readiness For

* Cloud Security Engineer
* GRC Analyst / Engineer
* Security Architect
* Risk & Compliance Lead
* Cloud Security Program Manager

This lab shows I can operate at the intersection of:

> **Engineering · Risk · Compliance · Leadership**

---

##  Why This Matters in 2025+

Cloud breaches aren’t just technical failures — they’re **governance failures**.

This lab proves I don’t just:

* Find issues
* Detect attacks

I can **design security programs that prevent them**.

---

##  Repository Structure

```
lab-06-cloud-grc-mapping/
├── analysis/
├── controls/
├── evidence/
│   └── screenshots/
└── README.md
```

---
