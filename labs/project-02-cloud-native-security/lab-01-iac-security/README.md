# Lab 1 — Insecure Terraform Deployment (Azure)

## Objective
Deploy intentionally misconfigured Azure infrastructure using Terraform
to simulate real-world cloud security exposure.

## What Was Deployed
- Azure Storage Account with public blob access
- Azure Kubernetes Service with public API endpoint
- RBAC and network protections intentionally disabled

## Skills Demonstrated
- Infrastructure as Code (Terraform)
- Azure cloud architecture
- Cloud security misconfiguration modeling
- Risk-focused security analysis

## Why This Matters
Cloud breaches often begin with misconfigured infrastructure.
This lab creates the attack surface required to demonstrate
identity abuse, policy enforcement, and CNAPP-style risk correlation
in later labs.

### Design-Time Security Validation

Infrastructure was intentionally not deployed due to Azure subscription constraints.
This lab demonstrates how cloud security engineers identify, document, and prevent insecure cloud configurations at design-time using Terraform — stopping risk before resources reach production.

### Evidence
Terraform plan execution was intentionally blocked due to missing Azure CLI authentication, demonstrating secure design-time review and deployment gating prior to cloud resource creation.
