# Cloud GRC Control Mapping

## Scope
This document maps Project 2 technical findings (IaC, IAM, Kubernetes, CNAPP)
to industry-standard security frameworks.

---

## Mapped Control Domains
- Infrastructure as Code (Terraform)
- Identity & Access Management (Entra ID)
- Kubernetes Security
- Runtime Threat Detection
- CNAPP Risk Correlation

---

## Example Mapping

| Technical Finding | Framework | Control ID | Description |
|------------------|----------|------------|-------------|
| Public Storage Account | NIST 800-53 | AC-3 | Access enforcement |
| Over-permissive IAM Role | CIS Azure | 1.1 | Least privilege |
| Insecure Pod Spec | CSA CCM | IVS-05 | Secure workload configuration |
| Runtime Shell Execution | NIST 800-53 | SI-4 | System monitoring |
