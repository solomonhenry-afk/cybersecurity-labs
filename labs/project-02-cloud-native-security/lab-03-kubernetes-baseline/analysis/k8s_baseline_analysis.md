# Kubernetes Baseline Security Analysis

## Overview
This lab demonstrates common Kubernetes workload misconfigurations that violate baseline security controls and expose clusters to container escape, privilege escalation, and lateral movement risks.

## Key Findings

### 1. Privileged Container Execution
The pod is deployed with `privileged: true`, granting the container access to host-level resources.

**Impact:**
- Container breakout potential
- Host compromise
- Full cluster takeover if combined with weak RBAC

---

### 2. Root User Execution
The container runs as UID 0 (`runAsUser: 0`).

**Impact:**
- Expanded attack surface
- Increased severity of container compromise
- Violates Kubernetes Pod Security Standards (Restricted)

---

### 3. Privilege Escalation Enabled
`allowPrivilegeEscalation: true` allows processes to gain additional Linux capabilities.

**Impact:**
- Attackers can elevate permissions inside the container
- Enables post-exploitation techniques

---

## Business Risk
If deployed in production, this configuration:
- Invalidates Zero Trust assumptions
- Creates regulatory and audit risk
- Amplifies blast radius of a single compromised workload

## CNAPP / Defender Mapping
These misconfigurations are directly detected by:
- Microsoft Defender for Kubernetes
- Wiz Kubernetes Security
- Prisma Cloud Workload Protection
