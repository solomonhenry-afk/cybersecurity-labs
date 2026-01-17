# Lab 01 — Legacy Perimeter to Zero Trust Migration

## Objective
This lab evaluates a traditional perimeter-based network security model and designs a modern Zero Trust architecture that reduces breach impact, limits lateral movement, and enforces identity-aware access.

The goal is not tool deployment, but **decision-grade architecture** that aligns security controls to real-world threat behavior.

---

## Scope
- Enterprise hybrid environment (on-prem + cloud)
- Legacy VPN-based remote access
- Flat internal network with implicit trust
- Internet-facing applications and internal services

---

## Problem Statement
Legacy perimeter security assumes:
- Internal traffic is trusted
- VPN equals authentication
- Firewalls alone provide segmentation

These assumptions fail against modern threats such as:
- Credential theft
- Lateral movement
- Insider misuse
- Supply chain compromise

---

## Approach
This lab:
1. Assesses the current-state network security posture
2. Identifies Zero Trust gaps tied to business risk
3. Designs a target Zero Trust architecture
4. Defines enforceable traffic flows and policy points

---

## Business Impact
- Reduced blast radius during breaches
- Identity-driven access decisions
- Stronger audit and compliance posture
- Security architecture aligned to modern attack paths

This lab demonstrates how to move from **implicit trust to continuous verification**.
