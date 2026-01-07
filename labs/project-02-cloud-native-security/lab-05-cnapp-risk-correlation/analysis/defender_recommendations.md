# Defender for Cloud — Security Recommendations & Remediation Mapping

## Overview
This document maps the identified CNAPP attack path to
Microsoft Defender for Cloud security recommendations.

The goal is not alert closure —  
it is **attack path disruption**.

---

## Attack Path Summary (Defender View)

Defender correlated:
- Public Azure Storage exposure (CSPM)
- Over-permissioned Entra ID identity (CIEM)
- AKS posture weaknesses
- Kubernetes runtime execution signals

Severity: **Critical**

---

## Defender Recommendations by Control Plane

---

## 1️⃣ Storage Account — Public Access

**Defender Recommendation**  
> *Storage accounts should restrict public blob access*

- Defender Control: CSPM
- Resource: Microsoft.Storage/storageAccounts
- Risk: Data exposure, initial access vector

### Remediation Actions
- Disable public container access
- Enforce private endpoints
- Apply Azure Policy: `Deny public blob access`

### Business Impact
Prevents anonymous access and data exfiltration.
Eliminates the external entry point of the attack path.

---

## 2️⃣ Entra ID — Over-Permissioned Identity

**Defender Recommendation**  
> *Overly permissive identities should be restricted*

- Defender Feature: Permissions Management (CIEM)
- Principal: Entra ID application
- Issue: Contributor role at subscription scope

### Remediation Actions
- Replace Contributor with least-privilege role
- Scope access to resource group level
- Enforce PIM for elevated access
- Monitor service principals for privilege drift

### Business Impact
Prevents privilege escalation and lateral movement.
Reduces blast radius from identity compromise.

---

## 3️⃣ AKS — Public API Exposure

**Defender Recommendation**  
> *Kubernetes API server should not be publicly accessible*

- Defender Product: Defender for Containers
- Resource: Azure Kubernetes Service

### Remediation Actions
- Disable public AKS API endpoint
- Restrict access via private endpoint
- Enforce authorized IP ranges

### Business Impact
Prevents direct cluster access from the internet.
Removes attacker control-plane access.

---

## 4️⃣ Kubernetes — Pod Security Configuration

**Defender Recommendation**  
> *Kubernetes workloads should follow Pod Security Standards*

- Control: Kubernetes posture management
- Risk: Privilege escalation inside cluster

### Remediation Actions
- Enforce restricted Pod Security Standard
- Block privileged containers
- Disable hostPath mounts
- Require non-root containers

### Business Impact
Prevents container escape and node compromise.
Protects cluster integrity.

---

## 5️⃣ Runtime Execution Detection

**Defender Recommendation**  
> *Investigate suspicious container execution activity*

- Defender Signal: Runtime threat detection
- Alert Type: Container exec from untrusted source

### Remediation Actions
- Terminate affected pod
- Rotate secrets
- Audit cluster access logs
- Enable continuous runtime protection

### Business Impact
Stops active attacker behavior.
Prevents persistence and data theft.

---

## Executive Remediation Strategy

Defender prioritizes **attack path removal**, not isolated fixes:

1. Close public exposure
2. Restrict identity privileges
3. Lock down AKS control plane
4. Enforce workload security
5. Monitor runtime continuously

---

## Key Insight
Security posture improves fastest when
**one remediation breaks multiple attack paths**.

This is the core value of CNAPP.
