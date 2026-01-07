# Lab 5 — CNAPP Risk Correlation (Attack Path Analysis)

## Executive Summary
This lab demonstrates how individual cloud misconfigurations compound into
a critical attack path when correlated by a CNAPP platform.

No single issue here is novel.
The risk emerges from **correlation**.

This mirrors how Wiz, Defender for Cloud, and Prisma Cloud surface
“toxic combinations” rather than isolated findings.

---

## Attack Path Overview

### Entry Point — Public Infrastructure Exposure
- Azure Storage Account configured with public container access
- Identified via IaC scanning (Terraform)

This provides unauthenticated access to cloud resources and metadata.

---

### Identity Amplification — Entra ID & Azure RBAC
- Over-permissioned Entra ID application
- Contributor role assigned at subscription scope

This transforms a low-risk exposure into an identity-driven escalation path.

Identity is the blast-radius multiplier.

---

### Compute Compromise — AKS
- AKS API server publicly reachable
- Insecure pod specification allows exec and privilege abuse
- Runtime activity detected consistent with container breakout attempts

This matches real-world AKS compromise chains observed in cloud incidents.

---

## CNAPP Correlation Logic (Wiz-Style)

A CNAPP does not alert on each issue independently.

It correlates:
- Public exposure (CSPM)
- IAM privilege escalation paths (CIEM)
- Kubernetes misconfigurations
- Runtime threat signals

The result is a **single critical attack path**, not noise.

---

## Business Impact
- Unauthorized data access
- Potential cluster takeover
- Subscription-wide compromise risk

This is why CNAPP findings are prioritized over raw vulnerability counts.

---

## Defensive Takeaway
Cloud security is not about fixing everything.
It is about breaking attack paths.

This lab demonstrates the difference.
