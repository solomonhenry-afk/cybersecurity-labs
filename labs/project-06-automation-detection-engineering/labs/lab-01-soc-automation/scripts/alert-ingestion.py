# Simulated alert ingestion

alerts = [
    {
        "alert_id": "A-1001",
        "source": "SIEM",
        "type": "Suspicious Login",
        "asset_id": "WEB-01",
        "severity": "Medium"
    }
]

def ingest_alert(alert):
    print(f"Ingesting alert {alert['alert_id']} from {alert['source']}")

for alert in alerts:
    ingest_alert(alert)
