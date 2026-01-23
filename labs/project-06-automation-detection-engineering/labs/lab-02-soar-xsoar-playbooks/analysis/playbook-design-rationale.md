# Playbook Design Rationale

## Why These Playbooks
The selected incidents represent the highest-volume and highest-impact
SOC events across most enterprises.

- Phishing → primary initial access vector
- Malware → lateral movement and persistence risk
- Privileged abuse → fastest path to catastrophic breach

## Design Principles
- Automate what is safe and repeatable
- Gate actions that could disrupt business
- Preserve analyst judgment for edge cases

## Strategic Intent
These playbooks mirror how XSOAR playbooks are designed in mature SOCs:
structured logic, clear exits, and audit-ready decisions.
