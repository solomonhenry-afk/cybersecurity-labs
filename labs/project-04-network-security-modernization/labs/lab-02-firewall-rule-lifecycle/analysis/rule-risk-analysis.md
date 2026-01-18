# Firewall Rule Risk Analysis

## Objective
Identify risk introduced by firewall rules independent of vulnerability data.

## Risk Factors Considered
- Exposure (Internet-facing vs internal)
- Access scope (specific vs broad)
- Privileged services (SSH, RDP, database ports)
- Directionality (ingress vs egress)

## Risk Assessment Example

| Rule | Risk Level | Reason |
|----|-----------|--------|
| Any → Internal | High | Enables lateral movement |
| App → DB | Medium | Necessary but sensitive |
| Internal → Internet | Low | Logged and restricted |

## Key Insight
Firewall rules shape attack paths. Poorly scoped rules expand blast radius during compromise.

## Conclusion
Rule risk must be assessed continuously, not only during initial deployment.
