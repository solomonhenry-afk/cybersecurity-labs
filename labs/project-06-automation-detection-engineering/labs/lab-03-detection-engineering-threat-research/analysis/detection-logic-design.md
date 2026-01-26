# Detection Logic Design

Detection logic is designed using a **behavioral correlation model**.

### Data Sources
- Authentication logs
- Endpoint telemetry
- Network flow data
- Cloud access logs

### Core Detection Principles
- No single-event alerts
- Correlation across time, identity, and behavior
- Thresholds tuned to reduce noise

### Example Logic
- Successful authentication + new geography
- Followed by access to privileged resources
- Followed by abnormal data transfer volume

Detections are designed to be **portable and vendor-agnostic**, aligning with Detection-as-Code practices.
