# Cybersecurity Hands-On Labs

This repository contains enterprise-aligned cybersecurity labs mapped to real-world job roles including vulnerability management, cloud security, IAM, SOC automation, and GRC.

---

## 🧪 Project 2: Cloud-Native Security Engineering (Azure · IAM · Kubernetes)

A hands-on cloud security engineering project focused on **real-world misconfigurations, attack paths, and detection workflows** across Infrastructure-as-Code, Identity, and Kubernetes.

### Labs
- **Lab 1:** Insecure Terraform Deployment (Azure Storage + AKS)
- **Lab 2:** Entra ID & Azure RBAC Misconfiguration
- **Lab 3:** Kubernetes Baseline Security Assessment
- **Lab 4:** Kubernetes Runtime Threat Detection *(in progress)*
- **Lab 5:** CNAPP Risk Correlation (IaC + IAM + K8s)

📁 Project Repository:  
[`labs/project-02-cloud-native-security`](labs/project-02-cloud-native-security)


## Lab 1: Vulnerability Discovery with Asset Context Enrichment
- Tooling: Nmap, OpenVAS/Nessus (simulated), CVE analysis
- Focus: Asset context, risk prioritization, remediation strategy

This project is inspired from my active job hunt after throughly reviewing all Job description to know what industry looks out for from a SOC Analyst, this version is written to pass **all three audiences at once**:

* Recruiters (clarity, structure, confidence)
* Hiring managers (judgment, realism, signal)
* Engineers (technical credibility, evidence)

No fluff. No buzzword soup. This is **portfolio-grade**.

##  Overview

This lab demonstrates a **real-world vulnerability discovery and triage workflow**, combining active scanning, asset context enrichment, and risk-based prioritization.

Rather than treating vulnerability severity in isolation, findings are evaluated based on **business criticality, exposure, and data sensitivity**—mirroring how modern SOC and vulnerability management teams reduce organizational risk.

---

##  Objectives

* Perform live service discovery and vulnerability enumeration
* Capture audit-ready scan artifacts
* Enrich technical findings with asset and business context
* Apply analyst judgment to prioritize and deprioritize findings
* Deliver clean, reviewable evidence using GitHub best practices

---

##  Tools & Techniques

* **Nmap** — service discovery and vulnerability enumeration
  (`-sV`, `--script vuln`, `-oN`)
* **Vulners integration** — CVE and exploit reference mapping
* **Asset inventory correlation** — business context enrichment
* **Git/GitHub** — evidence handling and delivery discipline

---

##  Methodology

### 1. Vulnerability Discovery

Active scanning was performed against scoped assets to identify exposed services and known vulnerabilities.

Key actions:

* Service detection to identify running applications
* Vulnerability enumeration using Nmap NSE scripts
* Output captured in plaintext for audit and review

### 2. Asset Context Enrichment

Raw scan results were enriched using an asset inventory containing:

* Business unit ownership
* Asset criticality
* Data sensitivity classification
* Network exposure (internet-facing vs internal)

This enabled accurate differentiation between **technical severity** and **business risk**.

### 3. Risk-Based Triage

Findings were prioritized based on:

* Severity + exploitability
* Asset criticality
* External exposure
* Potential business impact

Not all vulnerabilities were escalated—**analyst judgment was applied** to identify accepted risk versus actionable findings.

---

## My Key Findings

### Prioritized Findings

* Internet-facing services running on business-critical assets
* Services with known CVEs and exploit references
* Assets supporting operational or security tooling (e.g., management interfaces)

### Deprioritized / Accepted Risk

* **Slowloris DoS (CVE-2007-6750)** identified on localhost-only services
  **Rationale:** Lab-scoped, non-production exposure with no external attack surface

This reflects standard enterprise practice where **context determines remediation urgency**.

---

##  Evidence & Artifacts

```
lab-01-vulnerability-discovery/
├── scans/
│   └── nmap_scan.txt              # Raw scan output
├── data/
│   ├── assets.csv                 # Asset inventory with business context
│   └── findings_summary.txt       # Analyst triage and decisions
├── evidence/
│   └── README.md                  # Screenshot and validation references
└── README.md                      # Lab overview (this file)
```

All artifacts are structured for **easy review by recruiters, auditors, and technical stakeholders**.

---

## As An Analyst Perspective

This lab intentionally avoids a “scan-and-dump” approach.

Key analyst behaviors demonstrated:

* Risk ≠ CVSS
* Business impact drives prioritization
* Not every finding requires escalation
* Decisions are documented and defensible

This reflects how SOC analysts and vulnerability engineers operate in production environments.

---

##  My Final Outcome

By completing this lab, I demonstrated:

* Vulnerability discovery and enumeration
* Asset context enrichment
* Risk-based vulnerability triage
* Evidence handling and documentation
* Professional GitHub delivery practices

This lab mirrors the **day-to-day responsibilities of a SOC analyst or vulnerability engineer**, not a theoretical exercise.
