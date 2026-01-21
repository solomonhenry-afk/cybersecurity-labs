# Simulated SOC triage logic

def triage(alert):
    if alert.get("asset_context", {}).get("criticality") == "High":
        decision = "Escalate"
    else:
        decision = "Review"

    print(f"Triage decision for {alert['alert_id']}: {decision}")

sample_alert = {
    "alert_id": "A-1001",
    "asset_context": {"criticality": "High"}
}

triage(sample_alert)
