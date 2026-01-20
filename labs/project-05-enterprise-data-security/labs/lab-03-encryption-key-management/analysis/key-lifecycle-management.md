# Key Lifecycle Management

## Key Management Principles
- Centralized key control via KMS/HSM
- Separation of duties between data owners and key administrators
- Least-privilege access to keys
- Full audit logging

## Key Lifecycle Stages

### Key Generation
- Keys generated using approved cryptographic standards
- No hardcoded or manually created keys

### Key Storage
- Keys stored in managed KMS or HSM
- No plaintext key storage in applications or code repositories

### Key Access
- Role-based access controls enforced
- Break-glass access logged and reviewed

### Key Rotation
- Automated rotation on defined intervals
- Immediate rotation upon suspected compromise

### Key Revocation & Destruction
- Revocation triggered by employee offboarding or breach
- Secure destruction logged for audit purposes

## Risk Reduction
Effective key lifecycle management directly limits the blast radius of both insider threats and external breaches.
