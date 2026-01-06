### Investigation Summary

Runtime alert triggered due to execution of untrusted binaries inside a Kubernetes pod.

Findings:
- Interactive shell activity observed
- Outbound network call to suspicious IP
- Execution of downloaded payload

Impact:
- Potential container compromise
- Possible lateral movement risk
- Cluster-level exposure if RBAC is weak

Recommended Actions:
- Enforce runtime policies (Falco / Defender)
- Disable shell access in production pods
- Restrict egress traffic
- Apply least-privilege RBAC
