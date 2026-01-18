# Blast Radius Assessment

## Objective
Evaluate the potential impact if a firewall rule is abused following initial compromise.

## Assessment Approach
For each high-risk rule:
- Identify reachable systems
- Determine privilege escalation paths
- Evaluate data exposure potential

## Example
If an attacker compromises a web server:
- Rule allows access to internal admin network
- Enables lateral movement
- Expands incident scope significantly

## Before vs After Governance
- Before: Broad access, high blast radius
- After: Segmented access, constrained movement

## Conclusion
Reducing blast radius is as critical as preventing initial access.
