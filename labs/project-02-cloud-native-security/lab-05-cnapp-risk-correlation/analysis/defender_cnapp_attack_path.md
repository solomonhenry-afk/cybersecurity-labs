# Lab 5 — Azure Defender CNAPP Attack Path Analysis

## Executive Summary
This lab models how Microsoft Defender for Cloud correlates
infrastructure exposure, identity risk, and Kubernetes runtime signals
into a single critical attack path.

Individually, each issue is common.
Correlated, they represent a cloud breach-in-progress.

---

## Defender Correlation Overview

### 1. Initial Exposure — CSPM Finding
**Defender for Cloud** identifies a publicly accessible Azure Storage container
via CSPM continuous assessment.

- Resource Type: Microsoft.Storage/storageAccounts
- Risk: Unauthorized data access
- Signal Source: IaC posture + control plane visibility

This establishes the external entry point.

---

### 2. Identity Amplification — CIEM
**Defender Permissions Management** detects an over-permissioned
Entra ID application with Contributor access at the subscription scope.

This enables:
- Resource modification
- Lateral movement
- Privilege escalation

Identity transforms exposure into compromise.

---

### 3. Compute Layer Compromise — Defender for Containers
**Defender for Containers** correlates:
- Public AKS API endpoint
- Insecure pod security configuration
- Runtime exec activity inside a container

This matches known AKS attack techniques observed in cloud incidents.

---

## CNAPP Attack Path Logic (Defender View)

Defender does not surface these as isolated alerts.

It correlates:
- CSPM (public exposure)
- CIEM (identity privilege)
- Kubernetes posture
- Runtime threat signals

Result:
> **One Critical Attack Path**
> Subscription-wide impact possible

---

## Business Impact
- Data exposure from storage accounts
- Kubernetes cluster takeover
- Full subscription compromise potential

This is why Defender prioritizes attack paths over alert volume.

---

## Defensive Insight
Cloud security effectiveness is measured by
**attack paths broken**, not alerts closed.

This lab demonstrates Defender’s CNAPP value in practice.
