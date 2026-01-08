# NIST SP 800-53 Control Mapping — Cloud-Native Security Risks

## Purpose
This document maps cloud-native security risks identified in Project 2
to relevant NIST SP 800-53 Rev. 5 controls.

---

## 1. Identity & Access Management (IAM)

### Risk
Excessive permissions in Azure Entra ID roles enable privilege escalation.

### Mapped Controls
- **AC-2** — Account Management  
- **AC-6** — Least Privilege  
- **IA-2** — Identification and Authentication  

### Cloud Context
Azure Entra ID role assignments and service principals.

### Expected Outcome
Only explicitly authorized identities can access cloud resources.

---

## 2. Infrastructure as Code (IaC)

### Risk
Insecure Terraform configurations expose storage and APIs publicly.

### Mapped Controls
- **CM-2** — Baseline Configuration  
- **CM-6** — Configuration Settings  
- **SA-10** — Developer Configuration Management  

### Cloud Context
Terraform-managed Azure resources.

---

## 3. Kubernetes Security

### Risk
Pods running as root and public API exposure increase attack surface.

### Mapped Controls
- **SC-7** — Boundary Protection  
- **SI-7** — Integrity Checks  
- **CM-7** — Least Functionality  

### Cloud Context
Azure Kubernetes Service (AKS).

---

## 4. Continuous Monitoring & Detection

### Risk
Lack of runtime visibility delays breach detection.

### Mapped Controls
- **SI-4** — System Monitoring  
- **IR-5** — Incident Monitoring  
- **AU-6** — Audit Review  

### Cloud Context
Defender for Cloud, CNAPP telemetry, runtime detections.

---

## Summary
These mappings demonstrate how cloud-native risks translate directly
into federally recognized security controls, enabling audit alignment
and executive risk reporting.
