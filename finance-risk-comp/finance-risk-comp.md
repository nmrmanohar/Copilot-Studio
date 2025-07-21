# Financial Services Risk & Compliance Copilot

This Compliance Copilot automates Know-Your-Customer onboarding, anomaly detection, policy Q&A, and SAR drafting. It leverages MCP-based AML services, Dataverse transaction storage, Azure OpenAI summarisation, multi-agent orchestration, and an autonomous nightly auditor.

## Objectives
* Accelerate KYC processing by 60 %
* Auto-flag high-risk transactions under AML rules
* Generate SAR drafts ready for compliance review

## Architecture
| Layer | Components |
|-------|------------|
| **Master Agent** | "Compliance Assistant" orchestrating KYC & Risk agents |
| **Data** | Dataverse transactions, Customer profiles |
| **Tools** | MCP AML-Score, SAR template generator |
| **Autonomous** | "Midnight Auditor" nightly scan |

## Prerequisites
* Copilot Studio tenant licence in "Compliance" environment.
* MCP server endpoint & API key.
* DLP policy blocking external export of transaction data.

## Sample Data
`SampleData/transactions.csv` – mock transactions.

## Key Components
### Topics
* **Start KYC** – ID verification workflow
* **Policy Question** – summarises rule from PDF

### Agent Flows
* **Evaluate AML Risk** – MCP call returns risk rating
* **Draft SAR** – OpenAI summarises case into Word template

### Generative Orchestration
If user types “Open account for ACME & check AML,” agent chains KYC → AML Risk → Draft SAR if high.

### Multi-Agent Flow
High-risk flagged by Risk Agent invokes Compliance Agent to assign human review queue.

### Autonomous Auditor
Runs nightly; scans >$10k transactions, flags risky, drafts SARs.

## Deployment
1. Import `finance-copilot.zip`.
2. Update MCP connection.
3. Publish flows; enable orchestration & Midnight Auditor schedule.
4. Simulate high-value txn to verify automated SAR draft.

## Files
| File | Purpose |
|------|---------|
| finance-copilot.zip | Solution export |
| SampleData/transactions.csv | Mock transactions |
| templates/SAR.docx | SAR template |
