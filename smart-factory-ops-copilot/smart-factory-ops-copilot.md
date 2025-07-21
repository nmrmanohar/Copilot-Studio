# Manufacturing Smart-Factory Operations Copilot

The Smart-Factory Copilot equips plant personnel with real-time equipment insights, predictive maintenance scheduling, and automated work order creation. It integrates Azure IoT Hub telemetry, Azure ML predictive models, Dynamics 365 Field Service, custom topics, agent flows, generative orchestration, multi-agent safety coordination, and an autonomous guardian agent.

## Scenario & Benefits
* Reduce unplanned downtime via predictive alerts
* Improve safety compliance through autonomous monitors
* Accelerate maintenance response with AI-driven work orders

## Architecture
| Layer | Components |
|-------|------------|
| **Master Agent** | "Plant Ops Assistant" orchestrates Maintenance & Safety agents |
| **Data** | Azure IoT Hub → Time Series Insights |
| **Tools** | Predictive ML endpoint, Field Service connector |
| **Autonomous** | "Plant Guardian" polls telemetry, creates work orders |

## Prerequisites
* Managed "SmartFactory" environment with Copilot Studio
* IoT Hub and ML endpoint URLs in Key Vault
* Field Service connector using OAuth

## Sample Data
`SampleData/telemetry.json` – vibration & temp readings.

## Key Components
### Topics
* **Get Machine Status** – pulls latest telemetry
* **Schedule Maintenance** – suggests timeslot
* **Report Safety Incident** – logs incident

### Agent Flows
* **Predict Failure** – ML call returns risk score
* **Create Work Order** – Field Service API

### Generative Orchestration
Handles request like “Check A1 risk and schedule maintenance if >0.7.”

### Multi-Agent Safety
Safety Agent pauses maintenance until incident resolved.

### Autonomous Guardian
Polls IoT; if vibration > threshold, triggers Predict Failure & Work Order flows, sends Teams alert.

## Deployment
1. Import `smartfactory-copilot-solution.zip`.
2. Configure IoT, ML, Field Service connections.
3. Publish flows; enable orchestration.
4. Deploy Plant Guardian (5-min schedule).
5. Inject high vibration to test auto work order.

## Files
| File | Purpose |
|------|---------|
| smartfactory-copilot-solution.zip | Solution export |
| SampleData/telemetry.json | Mock telemetry |
| scripts/deploy-flows.ps1 | Publish flows |
