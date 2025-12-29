from datetime import datetime
from collections import defaultdict
import re

log_file = "labs/lab-03-detection-engineering/logs/ssh_auth.log"

failed_attempts = defaultdict(list)
alerts = []

def parse_time(ts):
    return datetime.strptime(ts, "%Y-%m-%dT%H:%M:%SZ")

ip_regex = re.compile(r"from (\d+\.\d+\.\d+\.\d+)")

with open(log_file, "r") as f:
    for line in f:
        line = line.strip()

        # Skip empty or malformed lines
        if not line:
            continue

        parts = line.split()
        if len(parts) < 5:
            continue

        try:
            timestamp = parse_time(parts[0])
        except ValueError:
            continue

        ip_match = ip_regex.search(line)
        if not ip_match:
            continue

        ip = ip_match.group(1)

        if "Failed password" in line:
            failed_attempts[ip].append(timestamp)

        if "Accepted password" in line and ip in failed_attempts:
            recent_failures = [
                t for t in failed_attempts[ip]
                if (timestamp - t).seconds <= 300
            ]

            if len(recent_failures) >= 5:
                alerts.append({
                    "ip": ip,
                    "time": timestamp,
                    "failures": len(recent_failures)
                })

print("[+] Detection Results:")
for alert in alerts:
    print(
        f"ALERT: SSH brute-force compromise detected | "
        f"IP={alert['ip']} | "
        f"Failures={alert['failures']} | "
        f"Time={alert['time']}"
    )
