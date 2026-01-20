# Enforcement Decision Matrix

| Data Type | Channel | Risk Level | Enforcement Action | Business Rationale |
|----------|--------|------------|--------------------|-------------------|
| PII | Email | High | Block | Regulatory exposure |
| PHI | USB | High | Block | Compliance violation |
| Internal Docs | Cloud Sync | Medium | Alert | Productivity impact |
| Public Data | Any | Low | Allow | No material risk |

## Decision Principle
Enforcement decisions are driven by risk, not convenience.
Blocking is reserved for scenarios where data loss is unacceptable.
