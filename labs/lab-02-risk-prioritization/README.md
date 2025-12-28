Lab 2 — Risk-Based Prioritization & Executive Communication

-  Objective

This lab demonstrates how raw vulnerability data is transformed into business-aligned risk prioritization and communicated in a way that enables executive decision-making.

Rather than treating all vulnerabilities equally, this exercise focuses on identifying which findings represent material risk based on asset criticality, exposure, and data sensitivity.

-  Technical Approach

Ingested vulnerability and asset data via CSV

Implemented a weighted risk-scoring model using Python

Normalized factors including:

CVSS severity

Asset criticality

Exposure (internet-facing vs internal)

Data sensitivity

Generated ranked outputs with clear Critical / High / Low risk tiers

-  Risk Scoring Logic (High-Level)

Risk scores were calculated using a weighted model to prioritize vulnerabilities that posed the greatest business impact, not just technical severity.

This approach mirrors how enterprise security teams and MSSPs perform risk-based vulnerability management.

-  Key Findings

Internet-facing, high-criticality assets surfaced as Critical risks

Internal systems with strong compensating controls were deprioritized

Several findings were intentionally marked Low Risk to prevent alert fatigue

This demonstrates intentional trade-off decisions, not automated output.

-  Executive Outcome

The final output enables leadership to:

Focus remediation on assets that reduce real-world risk

Avoid wasting resources on low-impact findings

Align security actions with business priorities

-  Evidence

analysis/risk_scoring.py — scoring logic

data/vulnerabilities.csv — input dataset

evidence/executive_summary.md — leadership-ready narrative

-  Why This Matters

This lab reflects how modern security teams operate:

Risk ≠ CVSS

Detection without prioritization is noise

Clear communication is as important as technical accuracy
