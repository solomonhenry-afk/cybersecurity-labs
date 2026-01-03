# Lab 1 Findings — Insecure Azure Infrastructure

## Identified Misconfigurations

### 1. Public Azure Blob Storage
- Blob public access enabled
- No network restrictions or private endpoint

**Risk:**
Exposes sensitive data to anonymous access and data exfiltration.

---

### 2. Public AKS API Server
- Kubernetes control plane accessible over the internet
- No IP restrictions applied

**Risk:**
Enables brute-force, API abuse, and cluster takeover attempts.

---

### 3. RBAC Disabled on AKS
- role_based_access_control_enabled = false

**Risk:**
Lack of identity enforcement enables privilege escalation and lateral movement.

---

### 4. Missing Governance Controls
- No data classification
- No owner tags
- No environment protection policies

**Risk:**
Breaks compliance posture and complicates incident response.
