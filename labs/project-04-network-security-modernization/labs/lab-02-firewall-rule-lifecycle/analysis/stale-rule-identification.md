# Stale Firewall Rule Identification

## Definition
A stale rule is a firewall rule that remains active despite no longer supporting a valid business requirement.

## Indicators of Staleness
- No traffic hits over extended periods
- Deprecated applications or systems
- Orphaned ownership
- Temporary rules never removed

## Risk of Stale Rules
- Unexpected exposure during incidents
- Bypass of newer security controls
- Increased audit and compliance risk

## Example Scenario
A temporary vendor access rule remains active after contract termination, enabling unauthorized access months later.

## Recommendation
Stale rules must be flagged, reviewed, and removed as part of routine governance.
