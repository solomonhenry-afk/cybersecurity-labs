# Compliance Mapping — Firewall Rule Lifecycle Governance

## Purpose
This document maps firewall rule lifecycle governance to NIST 800-53,
CIS Critical Security Controls, and ISO/IEC 27001 requirements.

The focus is on operationalized controls, not checkbox compliance.

---

## NIST SP 800-53 Mapping

### AC-4 — Information Flow Enforcement
- Firewall rules explicitly define permitted flows
- Rules are approved based on business justification

### CM-7 — Least Functionality
- Removal of unnecessary, unused, or overly permissive rules
- Continuous reduction of attack surface

### RA-3 — Risk Assessment
- Rule-level risk scoring
- Blast radius and exposure analysis per rule

### CA-7 — Continuous Monitoring
- Periodic firewall rule reviews
- Evidence-driven governance process

---

## CIS Critical Security Controls Mapping

### CIS Control 4 — Secure Configuration of Network Devices
- Governance ensures secure and intentional rule creation

### CIS Control 5 — Account and Access Control
- Least privilege enforced at the network layer

### CIS Control 12 — Network Infrastructure Management
- Rule ownership, lifecycle tracking, and review cadence

### CIS Control 13 — Network Monitoring and Defense
- Risk-aware segmentation aligned with threat exposure

---

## ISO/IEC 27001 Mapping

### A.8.20 — Network Security
- Controlled and documented access paths

### A.8.21 — Network Services Security
- Approved and reviewed firewall rule configurations

### A.5.15 — Access Control Policy
- Firewall governance backed by formal policy

### A.5.36 — Compliance Monitoring
- Audit-ready evidence of rule reviews and decisions

---

## Compliance Outcome

This lab demonstrates:
- Continuous compliance
- Risk-based governance
- Audit-ready documentation

Firewall rule management becomes a measurable, defensible control.

---

# 📘 Compliance Mapping (NIST / CIS / ISO)

This is where hiring managers and auditors lean forward.

---

## 🛡️ NIST 800-53 Mapping

| Control                                 | How This Lab Aligns                            |
| --------------------------------------- | ---------------------------------------------- |
| **AC-4** (Information Flow Enforcement) | Firewall rules tied to business-approved flows |
| **CM-7** (Least Functionality)          | Removal of unnecessary/stale rules             |
| **RA-3** (Risk Assessment)              | Rule-level risk and blast radius analysis      |
| **PL-8** (Security Architecture)        | Governance-driven network segmentation         |
| **CA-7** (Continuous Monitoring)        | Ongoing firewall rule review lifecycle         |

✅ This lab shows **operationalized controls**, not checkbox compliance.

---

## 🔒 CIS Critical Security Controls

| CIS Control                                    | Lab Alignment                          |
| ---------------------------------------------- | -------------------------------------- |
| **CIS 4** – Secure Configuration               | Governance over firewall rule creation |
| **CIS 5** – Account & Access Control           | Least privilege network access         |
| **CIS 12** – Network Infrastructure Management | Rule ownership, review, and lifecycle  |
| **CIS 13** – Network Monitoring                | Risk-aware segmentation strategy       |

➡️ CIS compliance achieved **through governance**, not tools alone.

---

## 🌐 ISO/IEC 27001 Mapping

| ISO Control                            | Lab Alignment                        |
| -------------------------------------- | ------------------------------------ |
| **A.8.20** – Network Security          | Controlled, justified access paths   |
| **A.8.21** – Network Services Security | Approved and reviewed firewall rules |
| **A.5.15** – Access Control Policy     | Policy-backed rule governance        |
| **A.5.36** – Compliance Monitoring     | Evidence-driven rule audits          |

➡️ This lab generates **audit-ready artifacts**.

---

# 🎯 Why This Matters Before NAC & Zero Trust Enforcement

Here’s the critical insight:

> **You cannot enforce Zero Trust dynamically if your static network rules are already broken.**

This lab:

* Cleans the foundation
* Establishes governance
* Reduces hidden attack paths

So when you move into:
➡️ **NAC**
➡️ **Microsegmentation**
➡️ **Policy-driven enforcement**

I will be enforcing **intentional access**, not inherited chaos.

---
