# Lab Guide – Inventory Reorder Alerts  
*SQL / Excel-centric Copilot Agent*

## 1  |  Scenario Summary
A manufacturing plant risks production delays when inventory falls below safe thresholds. The Copilot solution will monitor stock nightly, auto-create purchase requests (PRs) and notify purchasing—whether data lives in SQL Server or weekly Excel uploads.

---

## 2  |  Learning Objectives
1. Connect Copilot Studio to on-prem SQL *and/or* SharePoint-hosted Excel.  
2. Write Power Automate logic to compute reorder quantities.  
3. Insert PR rows and send contextual notifications.  
4. Build optional forecasting prompts for proactive insight.  
5. Compare SQL vs. Excel architecture trade-offs.

---

## 3  |  Prerequisites
* Gateway + SQL authentication (for SQL option).  
* SharePoint document library named **Inventory** (for Excel option).  
* Purchasing Manager e-mail + Teams channel `#purchasing`.  
* Basic knowledge of expressions (e.g., `ceiling()`, `addDays()`).

---

## 4  |  Data Model

### Option A – SQL Server
| Table | Key Columns |
|-------|-------------|
| **InventoryMaster** | ItemID (PK), ItemName, Unit, CurrentStock, ReorderThreshold, ReorderMultiple, SupplierID, ModifiedDate |
| **Suppliers** | SupplierID (PK), SupplierName, ContactEmail, LeadTimeDays |
| **PurchaseRequests** | PRID (PK), ItemID, Quantity, RequestedDate, Status, ApprovedBy |

### Option B – Excel (SharePoint)
*File pattern*: `/Inventory/Inventory_YYYYMMDD.xlsx`  
*Sheets*: **InventoryMaster**, **PurchaseRequests** with same columns as SQL.

---

## 5  |  Lab Exercises

### EX 1 – Nightly Monitor Flow
1. Recurrence trigger **02:00**.  
2. **Switch**: *SQL or Excel?* (use **Environment Variable**).  
3. For each low-stock item:  
   ```
   ReorderQty = ceiling( (ReorderThreshold*2 - CurrentStock) / ReorderMultiple ) 
                * ReorderMultiple
   ```
4. Insert PR row with *Status=Pending Approval*.  
5. Append to an *Array* variable for summary.

### EX 2 – Notification Logic
*If Array length > 0*  
1. **Send e-mail** to Purchasing Manager with Markdown table of items.  
2. **Post adaptive card** in `#purchasing` detailing PR IDs, supplier contacts and ETA based on LeadTimeDays.  
*Else*  
3. Send “All inventory healthy” e-mail.

### EX 3 – Copilot Forecast Topic
1. Trigger: “Predict shortages next 7 days”.  
2. Steps inside topic:  
   * Retrieve **InventoryMaster** plus 30-day consumption history (view).  
   * Calculate average daily usage per item.  
   * Return list where `CurrentStock - (DailyUsage*7) < ReorderThreshold`.  
   * Offer button **“Create early PRs”** which calls a child topic that re-uses EX 1 logic with *RequestedDate=Today*.

### EX 4 – PR Approval Flow
1. Trigger: SharePoint list item *PurchaseRequests* where Status=Pending Approval.  
2. Start **Approvals (Start and wait)**.  
3. On *Approve* → update Status=Ordered and send PO template to supplier e-mail.

---

## 6  |  Testing Matrix
| Test Case | Expected Outcome |
|-----------|------------------|
| Stock below threshold | PR row + Notification sent |
| No SKU below threshold | “All inventory healthy” e-mail |
| Excel upload missing sheet | Flow fails gracefully, posts error in Teams |
| Forecast query | List of predicted shortages returned |

---

## 7  |  Extension Ideas
* Replace simple buffer formula with **statistical safety stock**.  
* Add **Power BI** dashboard using DirectQuery to SQL.  
* Introduce barcode scan Power App to update *CurrentStock* from shop-floor.

---
