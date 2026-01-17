# Target Zero Trust Architecture

## Design Principles
- Never trust, always verify
- Identity is the new perimeter
- Enforce least privilege everywhere
- Assume breach

---

## Core Architecture Components

### Identity Provider (IdP)
- Central authority for user and service identity
- MFA and conditional access enforced
- Feeds identity context into policy decisions

---

### Policy Enforcement Points (PEPs)
- Enforce access decisions at:
  - Application gateways
  - ZTNA brokers
  - Workload boundaries
- Decisions based on identity, device, and context

---

### ZTNA (Zero Trust Network Access)
- Replaces traditional VPN
- Grants application-level access only
- No network-level exposure

---

### Microsegmentation
- Workloads isolated by function and risk
- East–west traffic explicitly authorized
- Reduces lateral movement

---

### Telemetry & Logging
- Continuous monitoring of access decisions
- Centralized logging for audit and detection
- Feeds SOC and incident response workflows

---

## Outcome
Access is continuously evaluated, tightly scoped, and fully auditable.
