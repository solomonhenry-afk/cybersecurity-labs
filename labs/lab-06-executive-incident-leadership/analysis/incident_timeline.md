
# Incident Timeline — Operation SILENT BEACON

## Incident Classification
- Severity: SEV-1
- Environment: GovCloud-aligned Production
- Incident Type: APT Intrusion (C2 + Post-Compromise Activity)

---

## Timeline (UTC)

### T-00:00 — Initial Indicator
- DNS telemetry flags abnormal beaconing behavior from a production Linux workload.
- Beaconing frequency deviates from established baseline patterns.

### T+05 Minutes — Automated Correlation
- Detection logic correlates DNS anomalies with recent SSH authentication activity.
- Multiple failed SSH attempts followed by a successful login identified.

### T+12 Minutes — SOC Analyst Triage
- Tier 2 analyst validates alert fidelity.
- Confirms suspicious external IP reputation and low-and-slow C2 characteristics.

### T+20 Minutes — Escalation
- Incident escalated to Detection Engineering and Incident Response leadership.
- Preliminary classification upgraded to **Potential APT Activity**.

### T+30 Minutes — Scope Assessment
- Asset ownership and business criticality confirmed.
- No evidence of immediate data exfiltration detected.
- Lateral movement attempts blocked by network segmentation.

### T+45 Minutes — Executive Notification
- CISO and executive stakeholders briefed.
- Three response options presented:
  - Monitor and observe
  - Isolate affected asset (recommended)
  - Full environment shutdown

### T+60 Minutes — Executive Decision
- Decision made to isolate affected workload.
- Priority placed on containment and forensic preservation.

### T+65 Minutes — Containment
- Affected system isolated from network.
- SSH credentials rotated.
- DNS egress rules tightened.

### T+90 Minutes — Forensic Preservation
- Volatile memory and log artifacts preserved.
- Indicators of Compromise (IOCs) documented.

### T+120 Minutes — Threat Eradication
- No persistence mechanisms found.
- No evidence of data exfiltration confirmed.

### T+180 Minutes — Recovery
- System rebuilt from trusted baseline.
- Monitoring enhanced for recurrence detection.

### T+24 Hours — Post-Incident Review
- Executive debrief conducted.
- Detection logic improvements documented.
- Incident classified as **Contained with No Business Impact**.
