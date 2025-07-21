# Lab Guide – Customer Feedback Analysis  
*SharePoint-centric Copilot Agent*

## 1  |  Scenario Summary
A retail chain receives hundreds of customer comments per week across physical stores and online forms. A Copilot agent will auto-label sentiment & topic, escalate urgent issues, and produce weekly insight reports—all inside Microsoft 365.

---

## 2  |  Learning Objectives
1. Configure SharePoint lists for feedback ingestion.  
2. Use AI Builder / Azure Cognitive Services for sentiment & category prediction.  
3. Build a Copilot agent that enriches feedback items and routes tasks.  
4. Create **Power Automate** flows for escalations, weekly digest and ageing alerts.  
5. Surface insights in e-mail and Teams.

---

## 3  |  Prerequisites
* SharePoint Online site with *Feedback* list created.  
* Text Analytics resource or Power Platform AI Builder licence.  
* Teams channels for *Customer Service* and *Facilities*.  
* Access to Power Automate and Copilot Studio.

---

## 4  |  SharePoint Schema
| List | Key Columns | Notes |
|------|-------------|-------|
| **Feedback Submissions** | ID (Auto), CustomerName, StoreID (Lookup), SubmissionDate, Rating (1-5), FeedbackText, AttachmentLink, PredictedCategory, Sentiment, AI_Summary, AssignedTo, Status | Core feedback store |
| **Store Directory** | StoreID, StoreName, Region, Manager | Lookup target |

> **Choice columns**  
> *Sentiment*: Positive | Neutral | Negative  *Status*: New | Escalated | In Review | Resolved

---

## 5  |  Lab Exercises

### EX 1 – Data Intake
1. Import sample `.csv` with 30 historical feedback rows.  
2. Attach 3 sample photos to demonstrate AttachmentLink behaviour.

### EX 2 – AI Prediction Flow
1. Create **Instant Cloud Flow → When an item is created (Feedback Submissions)**.  
2. Add **AI Builder–Predict Sentiment** → map *FeedbackText*.  
3. Add **AI Builder–Category Classification** → custom model with five categories.  
4. Write results back to **PredictedCategory**, **Sentiment** and **AI_Summary**.  
5. Condition: if *Sentiment=Negative* AND *Rating≤2* → set *Status=Escalated* and *AssignedTo=Customer Service*.

### EX 3 – Copilot Enrichment Topic
1. Topic trigger: “Summarise feedback *{ID}*”.  
2. Steps:  
   * Retrieve SharePoint item by ID.  
   * Respond with adaptive card containing sentiment icon, summary, attachment preview and quick links *Assign*, *Resolve*, *Escalate*.

### EX 4 – Escalation Alerts
| Flow | Trigger | Actions |
|------|---------|---------|
| **Urgent Feedback** | When item modified where Status=Escalated | Post to `#customer-service-escalations` with 🚨 emoji and deep link. |
| **Facilities Routing** | Condition inside AI flow – *PredictedCategory=Store Cleanliness* | Set *AssignedTo=Facilities* and post card to `#facilities-alerts`. |

### EX 5 – Weekly Insight Report
1. Scheduled Flow (Mon 06:00).  
2. *Get items* where *SubmissionDate LastWeek* → group by **Sentiment** / **PredictedCategory**.  
3. Compose Markdown table → pass to **Draft with Copilot** for narrative.  
4. Send e-mail to Retail Ops leadership with top 5 negative excerpts and trend arrows.

### EX 6 – Ageing Monitor
1. Recurrence flow (Daily 15:00).  
2. Query items where *Status=Escalated* and *Modified<Today-2* → Teams mention to *AssignedTo*.

---

## 6  |  Testing Checklist
- Submit new feedback with low rating → confirm AI assigns *Negative* & escalates.  
- Verify Teams alert card content matches SharePoint data.  
- Confirm Weekly Insight e-mail summarises correct counts.

---

## 7  |  Stretch Goals
* Add **Power BI** sentiment trend visual embedded in SharePoint.  
* Train multi-label classifier to pick *two* categories per comment.  
* Auto-translate foreign-language feedback before analysis.

---
