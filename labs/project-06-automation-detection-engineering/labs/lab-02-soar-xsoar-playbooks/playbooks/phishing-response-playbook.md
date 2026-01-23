# Phishing Response Playbook

## Trigger
User-reported phishing email or SIEM alert.

## Automated Actions
- Extract sender, URLs, attachments
- Reputation lookup and sandbox checks
- Identify impacted users

## Human Approval Required
- User mailbox purge
- Domain blocking

## Closure Criteria
- No malicious payload OR
- Malicious indicators contained and documented
