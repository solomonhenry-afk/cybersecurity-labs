# Simulated SOAR Orchestration Engine

def orchestrate(alert_type, confidence):
    if alert_type == "phishing":
        return "Execute phishing playbook"
    elif alert_type == "malware" and confidence > 80:
        return "Execute malware containment with approval"
    elif alert_type == "privileged_abuse":
        return "Require human approval before action"
    else:
        return "Manual investigation required"

print(orchestrate("phishing", 90))
