import os

BASE_DIR = os.path.dirname(__file__)
LOG_PATH = os.path.join(BASE_DIR, "../logs/runtime_events.log")

alerts = []

with open(LOG_PATH) as log:
    for line in log:
        if "cmd=curl" in line or "payload.sh" in line:
            alerts.append(line.strip())

print("[+] Runtime Detection Results:")
for alert in alerts:
    print(f"ALERT: Suspicious container behavior detected | {alert}")
