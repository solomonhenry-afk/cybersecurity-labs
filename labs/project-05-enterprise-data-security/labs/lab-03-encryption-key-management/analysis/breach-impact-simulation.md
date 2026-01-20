# Breach Impact Simulation

## Scenario 1: Cloud Storage Exfiltration
An attacker gains access to a cloud storage bucket containing customer data.

### Without Encryption
- Data immediately readable
- Mandatory breach notification
- Regulatory penalties likely

### With Encryption + Managed Keys
- Exfiltrated data unreadable
- Keys remain protected in KMS
- Breach impact limited to access exposure, not data compromise

## Scenario 2: Insider Database Dump
A privileged user exports sensitive database records.

### Without Strong Key Controls
- Data usable immediately
- Insider risk realized

### With Encryption + Key Governance
- Exported data remains encrypted
- Access to keys logged and restricted
- Incident response can focus on access misuse rather than data loss

## Executive Conclusion
Encryption combined with strong key management transforms breaches from catastrophic events into manageable incidents.
