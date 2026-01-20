# Data Exfiltration Scenarios

## Scenario 1 — Insider Email Exfiltration
An employee attempts to email a spreadsheet containing customer PII to a personal account.

Risk:
- Regulatory violation
- Intentional or negligent insider threat

Control:
- Content inspection
- Automatic block with incident escalation

## Scenario 2 — Cloud Storage Misuse
Sensitive files uploaded to unauthorized cloud storage (e.g., personal Google Drive).

Risk:
- Loss of visibility and control
- Third-party exposure

Control:
- Conditional allow with alerting
- CASB-integrated DLP enforcement

## Scenario 3 — Endpoint Data Transfer
PHI copied to removable media.

Risk:
- Physical data loss
- Compliance breach

Control:
- Block or encrypt based on user role and justification
