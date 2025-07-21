# Lab Guide – Employee Onboarding Portal  
*Dataverse-centric Copilot Agent*

## 1  |  Scenario Summary
A mid-sized organisation wants to replace its e-mail-driven onboarding with an automated Copilot experience that guides HR and hiring-managers, creates Dataverse records, triggers downstream provisioning and keeps everyone informed.

---

## 2  |  Learning Objectives
1. Design a Dataverse data model that supports onboarding tasks, asset requests and approvals.  
2. Configure a Copilot agent with multi-turn *Conversational Intake* that writes to Dataverse.  
3. Build **Power Automate** flows that:  
   • provision IT accounts, security badges and training slots  
   • chase overdue tasks and re-assign when managers change  
4. Generate weekly status dashboards and on-demand PDF summaries.  
5. Practise monitoring, troubleshooting and iterative improvement of the agent.

---

## 3  |  Prerequisites
* Power Platform environment with Dataverse enabled.  
* Security role with **Environment Maker** + **System Customiser**.  
* Access to Teams and Outlook for notifications.  
* Sample users for IT, Security and Training.

---

## 4  |  Reference Data Model
| Table | Key Columns | Purpose |
|-------|-------------|---------|
| **Employees** | EmployeeID (PK), FirstName, LastName, Email, DepartmentID, RoleID, StartDate, Status | Master record per hire |
| **Departments** | DepartmentID, DepartmentName | Lookup for organisational grouping |
| **Roles** | RoleID, RoleName, DefaultTaskTemplateID | Maps each role to a task template |
| **OnboardingTaskTemplates** | TemplateID, TaskDefinitions (JSON) | Stores task blueprints per role/department |
| **OnboardingTasks** | TaskID, EmployeeID, TaskName, DueDate, Status, AssignedTo | Concrete tasks generated from template |
| **Assets** | AssetID, AssetName, Category, AssignedToEmployeeID, Status | Hardware / licence requests |
| **TrainingModules** | ModuleID, ModuleName, DeliveryMethod | Courses scheduled for new hire |
| **Approvals** | ApprovalID, EmployeeID, ApproverID, ApprovalType, Status | Tracks manager or IT sign-off |

> **Choice Sets**  
> *EmployeeStatus*: Onboarding | Active | Terminated  
> *TaskStatus*: Not Started | In Progress | Completed  
> *AssetStatus*: Requested | Ordered | Delivered  
> *ApprovalStatus*: Pending | Approved | Rejected

---

## 5  |  Lab Exercises

### EX 1 – Environment & Data Setup
1. **Import the solution** file provided by the instructor *or* manually create the eight tables above.  
2. Add sample Departments, Roles and TaskTemplates.  
3. Create Teams channels `#onboarding-it`, `#onboarding-security`, `#onboarding-training`.

### EX 2 – Build the Copilot *Conversational Intake*
1. Open **Copilot Studio → Create → Custom Copilot**.  
2. Add a **Topic** “Start Onboarding”.  
3. Draft system prompt:  
   ```
   You are HR Copilot. Collect full name, start date, department,
   role and special equipment. Use follow-up questions when data is missing.
   ```
4. Add Turn 1: Ask “Who are we onboarding and when do they start?” → save to variables.  
5. Invoke **Dataverse action** •Create a new *Employees* row• mapping fields.  
6. Add a second action **Custom Code** to:  
   * fetch the role template  
   * parse JSON **TaskDefinitions**  
   * bulk-insert rows into *OnboardingTasks*.

### EX 3 – Automation Flows
| Flow | Trigger | Key Actions |
|------|---------|-------------|
| **New Hire Kick-off** | Employees row where Status = Onboarding | 1. Send e-mail to IT, Security, Training. 2. Create approval rows for assets. 3. Post adaptive card in `#onboarding-it` summarising access needs. |
| **Overdue Task Reminder** | Recurrence (08:00 daily) | List *OnboardingTasks* where Status≠Completed & DueDate<Today → for each row send Teams mention to *AssignedTo*. |
| **Manager Re-assignment** | Employees row modified (ManagerID change) | Update open tasks’ AssignedTo; notify new manager. |

### EX 4 – Reporting & Insights
1. **Scheduled Cloud Flow** (Mon 07:00) → aggregate tasks by status via Dataverse list rows.  
2. Pass statistics to “Draft with Copilot” action → generate friendly e-mail.  
3. Use **Word Online (Business)–Populate Template** to create a branded PDF report.

### EX 5 – Validation
1. Trigger the topic with “I just hired Jane Doe …”.  
2. Confirm rows were written to all seven tables.  
3. Verify IT e-mail, Teams alerts and approvals.  
4. Mark a task overdue → ensure next day reminder.

---

## 6  |  Cleanup
* Change Employee.Status to **Active** (simulates completed onboarding) → watch emails stop.  
* Delete Employee row to remove cascade data if required.  

---

## 7  |  Further Exploration
* Integrate **Azure AD** Graph calls for real account provisioning.  
* Add Power BI *Onboarding Dashboard* filtered by Department.  
* Extend Approvals with *parallel* approval model for hardware vs. software.

---
