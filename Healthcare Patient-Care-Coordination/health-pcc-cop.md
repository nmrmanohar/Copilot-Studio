# Healthcare Patient-Care Coordination Copilot

The Healthcare Patient-Care Coordination Copilot addresses patient triage, appointment booking, medical records retrieval, billing inquiries, and proactive outreach within a unified Copilot Studio solution. Leveraging custom topics, agent flows, secure FHIR connectors, Model Context Protocol (MCP) integrations, generative AI, multi-agent orchestration, and autonomous scheduling triggers, this copilot streamlines clinician workflows and improves patient satisfaction.

## Architecture Overview

Five collaborating agents—Triage, Appointment, Records, Billing, Outreach—are coordinated by a Master Orchestrator. Each agent relies on topics, deterministic flows, and tools that access FHIR APIs, databases, and Azure OpenAI. Autonomous agents monitor lab orders and send follow-up messages.

## Prerequisites

* Copilot Studio tenant license
* Managed "Prod-Healthcare" environment
* DLP policy restricting PHI to FHIR endpoints
* PatientCareMonitor service principal with least-privilege access

## Data & Connector Setup

* Sample FHIR endpoint in `.env`
* SQL DB for appointments
* Azure OpenAI connection for summarization
* Sample JSON/CSV files in `SampleData`

## Key Components

### Topics
* "Chief Complaint" – captures free-text symptoms
* "Check Availability" & "Book Appointment" – schedule visits

### Agent Flows
* **Find Next Slot** – SQL query → return time options
* **Validate Insurance** – MCP call → eligibility response

### Tools
* FHIR Patient, Observation, Appointment APIs
* Billing validation tool via MCP

### Generative Orchestration
Master agent chains record lookup → appointment booking → billing check based on intent.

### Multi-Agent Collaboration
High-risk symptoms trigger Outreach Agent for nurse follow-up.

### Autonomous Agents
Lab Monitor polls FHIR Observations; threshold breach triggers notification flow.

## Deployment Steps
1. Import `healthcare-copilot-solution.zip` into Prod-Healthcare.
2. Update connection references for FHIR & OpenAI.
3. Publish agents and flows; enable generative orchestration.
4. Schedule Lab Monitor agent.
5. Test triage → booking → billing and autonomous alert scenarios.

## Provided Files
| File | Purpose |
|------|---------|
| healthcare-copilot-solution.zip | Exported solution |
| SampleData/patientList.json | Mock patients |
| SampleData/appointments.csv | Appointment history |
| scripts/setup-env.ps1 | Environment setup |
