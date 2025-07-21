# Logistics Supply-Chain Fulfilment & Route Optimisation Copilot

This logistics copilot assists dispatchers with dynamic route optimisation, real-time driver support, and customer shipment tracking. It integrates Bing Maps, MQTT telematics, Dynamics 365 SCM, custom topics, agent flows, generative orchestration, multi-agent collaboration, and an autonomous Cold-Chain Guard.

## Business Need
* Optimise routes to reduce delivery time & fuel cost
* Provide driver support & proactive customer notifications
* Maintain temperature compliance for cold-chain cargo

## Architecture
| Layer | Components |
|-------|------------|
| **Master Agent** | "Logi-Ops" orchestrates Route, Driver, Customer agents |
| **Data** | Bing Maps traffic, MQTT GPS feed, Dynamics SCM orders |
| **Tools** | Route Optimiser, Notify Customer flow |
| **Autonomous** | Cold-Chain Guard temperature monitor |

## Prerequisites
* Copilot Studio in "LogisticsOps" environment
* Bing Maps API key, MQTT broker creds, Dynamics OAuth
* DLP locking shipment data internally

## Sample Data
`SampleData/telematics.json` – GPS & temperature.

## Key Components
### Topics
* **Plan Route** – calculates best path
* **Driver Support Query** – handles issues
* **Track Shipment** – provides ETA

### Agent Flows
* **Reroute Shipment** – GPS+traffic → optimise route → update SCM → notify
* **Notify Customer** – sends email/Teams update

### Generative Orchestration
Handles “Truck 12 stuck in rain—reroute & tell customer.”

### Multi-Agent Collaboration
Driver & Customer agents invoked based on delay severity.

### Autonomous Cold-Chain Guard
Monitors temperature; if >threshold, triggers reroute & incident log.

## Deployment
1. Import `logistics-copilot.zip`.
2. Configure Bing Maps, MQTT, Dynamics connectors.
3. Publish flows; enable orchestration & Cold-Chain Guard schedule.
4. Simulate delay & temp breach to validate.

## Files
| File | Purpose |
|------|---------|
| logistics-copilot.zip | Solution export |
| SampleData/telematics.json | Mock telematics |
| scripts/deploy-log-connectors.ps1 | Setup connectors |
