# Current-State Network Security Assessment

## Overview
The existing environment relies on a traditional perimeter-based security model designed for static, on-prem networks.

This model introduces significant risk in modern hybrid and remote-first environments.

---

## Key Characteristics Observed

### 1. Perimeter-Centric Trust
- Strong controls at the network edge
- Minimal inspection of internal east–west traffic
- Internal systems implicitly trusted once inside

### 2. VPN as Primary Access Control
- VPN access grants broad network reachability
- Limited application-level authorization
- No continuous verification after connection

### 3. Flat or Over-Permissive Segmentation
- Large trusted network zones
- Firewall rules prioritize connectivity over least privilege
- High lateral movement potential

### 4. Limited Identity Context
- Network decisions based on IP and port
- No device posture validation
- Weak linkage between user identity and access policy

---

## Risk Implications
- Stolen credentials lead to wide internal access
- Malware can move laterally without resistance
- Insider actions are difficult to constrain or audit
- Breach detection occurs late in the attack lifecycle

This posture is misaligned with modern threat behavior.
