# Lab Guide – Sales Opportunity & Support Portal  
*Dataverse + SharePoint Hybrid Copilot Agent*

## 1  |  Scenario Summary
Sales reps work in Dynamics 365; Support engineers reference SharePoint docs. A unified Copilot agent will surface opportunities, contracts and open tickets in a single chat, while automating high-priority alerts and project kick-offs.

---

## 2  |  Learning Objectives
1. Federate data from Dataverse (D365) and SharePoint libraries inside one Copilot.  
2. Implement multi-persona dialogues for Sales vs. Support context.  
3. Create document retrieval actions using Graph API.  
4. Build complex **Power Automate** flows for escalations and won-deal hand-offs.  
5. Demonstrate proactive “at-risk deal” insights and KB article broadcasts.

---

## 3  |  Prerequisites
* D365 Sales with sample data (Accounts, Opportunities).  
* SharePoint libraries **Proposals**, **Contracts**, **SupportKB**.  
* Teams channels `#sales-alerts`, `#support-escalations`, `#project-launch`, `#kb-announcements`.  
* Graph API consent for `Sites.Read.All`, `Files.ReadWrite.All`.

---

## 4  |  Data Sources
### Dataverse Entities
Accounts, Contacts, Opportunities, Activities, SupportCases.

### SharePoint Libraries
| Library | Folder Strategy | Key Metadata |
|---------|-----------------|--------------|
| **Proposals** | `/Proposals/{Account}` | DocumentType, UploadDate |
| **Contracts** | `/Contracts/{Account}` | Signed (Yes/No), SignedDate |
| **SupportKB** | single-level | KBID, Category, PublishedDate |

---

## 5  |  Lab Exercises

### EX 1 – “Opportunity Status” Topic
1. Trigger: “Status of opportunity *{OppName}*”.  
2. Steps:  
   * Query *Opportunities* by *Name*.  
   * Retrieve stage, probability, estimated revenue, close date.  
   * Follow-up question if multiple matches.  
3. Reply with adaptive card including **stage colour bar** and latest *Activity* summary.

### EX 2 – “Open Support Cases” Topic
1. Trigger: “Open cases for *{AccountName}*”.  
2. Return bullet list with Owner, Priority badge and open duration.  
3. Quick Actions: **“Assign to me”**, **“Escalate”** (updates Priority=High).

### EX 3 – Document Retrieval Action
1. Input: *AccountName* + DocumentType (“latest proposal” or “signed contract”).  
2. Action:  
   * Call **Graph List DriveItems** on target folder.  
   * Order by *UploadDate desc*.  
   * Return file card with link and *Open in Word* button.

### EX 4 – Automated Flows
| Flow | Trigger | Steps |
|------|---------|-------|
| **High-Priority Support Escalation** | SupportCases row where Priority=High & Status=Active | 1. Post alert in `#support-escalations` with 🔴 badge. 2. E-mail Account.PrimaryContact with ETA template. |
| **Opportunity Won → Project Kick-Off** | Opportunities stage changes to Won | 1. Copy signed contract to `/Client Projects/{Account}`. 2. Create *Project* entity + default *ProjectTasks*. 3. Post celebration GIF in `#project-launch` and tag PM. |
| **At-Risk Deal Digest** | Scheduled 07:00 daily | Query open opps closing in 7 days & Probability<50 → Compose Copilot summary; Teams post in `#sales-alerts`. |
| **New KB Article Announcement** | File created in **SupportKB** where Category=Troubleshooting | Generate teaser text via Copilot; post in `#kb-announcements`. |

### EX 5 – Multi-Persona Switch
Add **Condition** in root topic:  
```
if caller.Department = 'Support' then load sub-topic group 'Support'
else load 'Sales'
```
Each group has tailored tone, synonyms and quick replies.

---

## 6  |  End-to-End Test Script
1. **Sales Rep** asks opportunity status → verify Dataverse data.  
2. Upload new signed contract → agent copies & confirms path.  
3. **Support Engineer** escalates a case → Teams alert fires.  
4. Mark opportunity *Won* → project kick-off flow triggers; contract copied.

---

## 7  |  Enhancements
* Enable **semantic search** across SharePoint + Dataverse using Copilot extensions.  
* Add Viva Sales plugin to log calls automatically as *Activities*.  
* Gamify sales behaviour: push adaptive card leaderboard in `#sales-alerts`.

---
