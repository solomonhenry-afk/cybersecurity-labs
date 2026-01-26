# Threat Hypothesis

This lab is based on the following threat assumptions:

1. Initial access is often achieved via:
   - Phishing
   - Credential reuse
   - Token theft

2. Once inside, attackers prioritize:
   - Privilege escalation
   - Lateral movement
   - Data staging prior to exfiltration

3. Most damage occurs **after initial access**, not during it.

### Primary Hypothesis
If an attacker successfully authenticates using stolen credentials, they will:
- Authenticate from unusual locations or devices
- Access resources outside normal behavioral baselines
- Attempt lateral movement or data aggregation

This lab focuses on detecting **post-compromise behavior**, where defenders still have time to act.
