# Retail Omnichannel Customer Service & Returns Copilot

This retail copilot delivers unified customer service across chat, web, in-store kiosks, and phone, handling order status, returns/exchanges, product Q&A, and loyalty rewards. It combines custom topics, Power Automate agent flows, Shopify & Azure SQL tools, Model Context Protocol (MCP) for inventory checks, generative orchestration, multi-agent collaboration, and an autonomous insights agent that reacts to declining NPS scores.

## Architecture Snapshot

| Layer | Components |
|-------|------------|
| **Master Agent** | "Retail CX Assistant" orchestrating sub-agents |
| **Sub-Agents** | Order-Lookup, Returns/Exchange, Product-FAQ, Loyalty-Points |
| **Data** | Azure SQL orders DB, Shopify API, SharePoint product KB, Loyalty service |
| **Tools** | Refund policy prompt, label-gen flow plugin, MCP inventory lookup |
| **Autonomous** | "Return-Insight" monitors CSAT & triggers offers |

## Prerequisites

* Copilot Studio tenant license in a managed "RetailCX" environment.
* API credentials for Shopify, Loyalty service, and SharePoint stored in Azure Key Vault.
* DLP policy restricting external connectors.

## Sample Data
* `SampleData/orders.csv` – mock order history.
* `SampleData/products.csv` – product catalog.
* `SampleData/chat-transcripts.json` – historical queries for topic tuning.

## Key Components

### Topics
* **Track Order Status** – triggers via “Where is my order?”
* **Initiate Return** – triggers via “Start a return.”
* **Product Compatibility** – FAQs, uses SharePoint KB.
* **Check Loyalty Balance** – retrieves points.

### Agent Flows
* **Create Return Label** – Power Automate flow generates PDF, stores in SharePoint, returns link.
* **Issue Refund** – invokes Shopify refund API and confirms.

### Tools & MCP Integration
* Shopify Order connector
* SharePoint Document connector
* Loyalty Points connector
* MCP inventory check tool (inputs: SKU, qty)

### Generative Orchestration
Handles compound queries like “Shoes don’t fit—return and reorder size 9.” Plans Order-Lookup → Returns → Inventory check → Loyalty suggestion.

### Multi-Agent Collaboration
If item OOS, Master hands off to Loyalty-Points agent to propose voucher.

### Autonomous Insights Agent
Scheduled daily; if NPS < 8, auto-invokes Loyalty-Points to issue coupon.

## Deployment Steps
1. Import `retail-copilot-solution.zip` into RetailCX.
2. Configure connection references for Shopify, SharePoint, Loyalty API.
3. Publish sub-agents; enable generative orchestration.
4. Test Create Return Label flow.
5. Enable Return-Insight autonomous agent; validate NPS trigger.

## Provided Files
| File | Description |
|------|-------------|
| retail-copilot-solution.zip | Full solution export |
| SampleData/orders.csv | Mock orders |
| SampleData/products.csv | Product catalog |
| scripts/configure-connectors.ps1 | Setup script |
