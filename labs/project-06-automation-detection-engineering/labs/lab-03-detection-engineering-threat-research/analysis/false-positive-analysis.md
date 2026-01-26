# False Positive Analysis

False positives are treated as **operational risk**.

### Common Legitimate Scenarios
- VPN usage by remote employees
- IT administrators performing maintenance
- Automated service accounts

### Mitigation Strategies
- Identity-based allowlists
- Time-of-day analysis
- Role-aware thresholds

Each detection includes documented tuning decisions to balance:
- Coverage
- Analyst workload
- Response confidence
