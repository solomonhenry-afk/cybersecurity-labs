# Encryption Coverage Analysis

## Overview
This analysis identifies where encryption is enforced, where gaps exist, and the business risk associated with each gap.

## Coverage Areas Reviewed
- Databases (PII, PHI, financial data)
- Cloud object storage
- Backups and snapshots
- SaaS data repositories
- Data in transit (API, user access)

## Findings
- Core production databases are encrypted at rest using platform-native encryption.
- Backups inherit encryption inconsistently across environments.
- Certain SaaS exports rely on vendor-managed encryption with limited visibility.
- Encryption in transit is enforced for external access but inconsistently for internal service-to-service communication.

## Risk Implications
- Unencrypted backups represent high-impact breach scenarios.
- Weak internal encryption increases insider and lateral movement risk.
- Lack of visibility into SaaS encryption shifts risk to contractual controls.

## Recommendation
Encryption must be enforced consistently and paired with centralized key governance to ensure risk reduction is real, not assumed.
