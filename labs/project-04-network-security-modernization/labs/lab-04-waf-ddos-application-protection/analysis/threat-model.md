# Application Threat Model

## Threat Actors
- Botnets targeting availability
- Credential stuffing groups
- Opportunistic scanners exploiting OWASP Top 10
- Targeted actors abusing business logic

## Key Attack Vectors
- HTTP flood (Layer 7 DDoS)
- SQL injection / XSS
- API abuse and enumeration
- Authentication brute force

## Business Impact Mapping
| Threat | Impact |
|------|--------|
| App downtime | Revenue loss, SLA breach |
| Account takeover | Fraud, data exposure |
| API abuse | Service degradation |
| Injection attacks | Data integrity loss |

## Risk Insight
Application attacks bypass traditional perimeter defenses and directly affect customer trust and revenue.

Proves Mapping of:

- OWASP Top 10

- App-layer DDoS

- Credential stuffing

Which threats are stopped by WAF

Which require rate limiting / upstream controls
