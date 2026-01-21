# Alert Enrichment Strategy

## Problem
Raw alerts lack context:
- No asset criticality
- No business impact
- No threat relevance

This forces analysts to manually pivot across tools, increasing MTTR.

## Enrichment Dimensions
Each alert is enriched with:

1. Asset Context
   - Asset name
   - Environment (prod / dev)
   - Business criticality

2. Threat Intelligence
   - Known exploitation status
   - Malware / TTP association
   - Adversary targeting profile

3. Risk Signals
   - Exposure (internet-facing vs internal)
   - Data sensitivity
   - Historical alert frequency

## Result
Alerts become **incidents**, not noise — enabling faster, defensible decisions.
