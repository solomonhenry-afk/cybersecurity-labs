# Zero Trust Traffic Flow Definitions

## 1. Authorized User → Application
1. User authenticates via IdP with MFA
2. Device posture is validated
3. Policy decision evaluates identity, role, device, and context
4. ZTNA broker establishes application-specific access
5. Traffic is logged and monitored

---

## 2. Unauthorized Access Attempt
1. Authentication fails or policy conditions not met
2. Access is denied before reaching the application
3. Event is logged for security review

---

## 3. Service-to-Service Communication
1. Services authenticate using workload identity
2. Mutual authentication enforced
3. Only explicitly allowed service flows permitted
4. Traffic inspected and logged

---

## 4. Internet Egress Traffic
- Egress routed through secure inspection point
- Policy enforces destination and protocol restrictions
- Logging enabled for anomaly detection

---

## 5. Enforcement Visibility
- All flows generate telemetry
- Logs feed SOC, SIEM, and audit processes

---

## Summary
Traffic is no longer implicitly trusted. Every flow is explicitly authorized, inspected, and logged.
