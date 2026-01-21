# Simulated alert enrichment

asset_inventory = {
    "WEB-01": {
        "criticality": "High",
        "environment": "Production",
        "business_owner": "E-Commerce"
    }
}

def enrich_alert(alert):
    asset = asset_inventory.get(alert["asset_id"], {})
    alert["asset_context"] = asset
    return alert

print("Alert enriched with asset context")
