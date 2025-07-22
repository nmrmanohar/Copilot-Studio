# Healthcare Copilot Studio Agent - Detailed Step-by-Step Guide

## Prerequisites
1. **Azure Subscription & Licenses**
   - Active Azure subscription with Power Platform and Copilot licenses.
   - Access to Power Apps Maker portal (https://make.powerapps.com).
2. **Environment Setup**
   - Create or select an environment named `HealthcareEnv`.
   - Ensure Dataverse and SharePoint connectors are enabled.
3. **SharePoint Site**
   - A SharePoint modern site (e.g., `https://contoso.sharepoint.com/sites/Healthcare`).
   - Create a document library named `KnowledgeDocs`.

---

## 1. Create Dataverse Tables
### 1.1 Patient Table
1. In the Maker portal, select **Data** > **Tables** > **New table**.
2. Name: **Patient**; Primary column: **FullName**.
3. Add columns:
   - **PatientID** (Text, Required)
   - **DOB** (Date and Time)
   - **Gender** (Choice: Male, Female, Other)
   - **Email** (Email)
   - **Phone** (Phone)
4. Save and publish.

### 1.2 Appointment Table
1. **Data** > **Tables** > **New table**.
2. Name: **Appointment**; Primary column: **AppointmentID**.
3. Add columns:
   - **PatientID** (Lookup to Patient)
   - **AppointmentDate** (Date and Time)
   - **Doctor** (Text)
   - **Department** (Text)
   - **Notes** (Multiline Text)
4. Save and publish.

### 1.3 Medication Table
1. **Data** > **Tables** > **New table**.
2. Name: **Medication**; Primary column: **MedicationID**.
3. Add columns:
   - **PatientID** (Lookup to Patient)
   - **MedicationName** (Text)
   - **Dosage** (Text)
   - **StartDate** (Date)
   - **EndDate** (Date)
4. Save and publish.

---

## 2. Upload Sample Documents to SharePoint
1. Go to `KnowledgeDocs` library in your SharePoint site.
2. Create `Patient_Guide.docx`, `Appointment_Process.docx`, `Medication_FAQ.docx`.
3. Upload these files.

---

## 3. Provision Copilot Studio Project
1. In Power Apps Maker portal, select **AI Studio** > **Copilot Studio (Preview)**.
2. Click **New project**, name: `HealthcareAssistant`.
3. Select environment: `HealthcareEnv`.
4. Choose **Create**.

---

## 4. Define Topics & Entities
### 4.1 Add Topic: PatientInformation
1. In **Topics** tab, click **+ Add topic**.
2. Name: `PatientInformation`.
3. Define **Entities**:
   - **Patient** (Link to Dataverse `Patient` table).
   - Synonyms: `patient`, `client`.
4. Add sample utterances:
   - “Show me patient details for John Doe.”
   - “Get info on patient P001.”

### 4.2 Add Topic: ScheduleAppointment
1. **+ Add topic**, Name: `ScheduleAppointment`.
2. Entities:
   - **Patient** (lookup).
   - **AppointmentDate** (datetime).
3. Utterances:
   - “Schedule an appointment for Jane Smith on August 1st.”
   - “Book cardiac appointment on 2025-08-05 at 10 AM.”

---

## 5. Configure Generative Orchestration
1. In **Orchestration** tab, click **+ Add orchestration**.
2. Name: `HealthcareGenOrch`.
3. Add steps:
   - **Call LLM** for summarization of patient history.
   - **Invoke connector** to fetch records from Dataverse.
   - **Call LLM** to generate recommendations.

---

## 6. Build Agent Flows
### 6.1 Patient Lookup Flow
1. In **Agent Flows**, click **+ New flow**.
2. Trigger: **OnTopicDetected** = `PatientInformation`.
3. Steps:
   - **Dataverse Retrieve**: Fetch `Patient` record by `PatientID`.
   - **Compose**: Format response text.
   - **Return**: Send back patient details.

### 6.2 Appointment Scheduler Flow
1. **+ New flow**, Trigger: `ScheduleAppointment`.
2. Steps:
   - **Dataverse Create**: Create record in `Appointment` table.
   - **Send Email**: Notify patient (configure connector).
   - **Return**: Confirmation message.

---

## 7. Add Connector & Prompt Tools
1. **Connector Tools**:
   - **Dataverse**: CRUD operations for tables.
   - **SharePoint**: Read documents from `KnowledgeDocs`.
2. **Prompt Tools**:
   - **SummarizeDocument**: LLM call to summarize a SharePoint doc.
   - **GenerateFollowUp**: LLM to suggest next steps.

---

## 8. Setup Autonomous Agents
1. In **Autonomous** tab, click **+ New agent**.
2. Name: `MedicationReminder`.
3. Define:
   - **Trigger**: Scheduled daily at 8 AM UTC.
   - **Action**: Query `Medication` table for active meds.
   - **Send Message**: Format and send reminders to patient emails.

---

## 9. Multi-Agent Orchestration
1. **Orchestration** > **Multi-agent** > **+ New orchestration**.
2. Include:
   - **PatientLookupAgent**
   - **AppointmentScheduler**
   - **MedicationReminder**
3. Define sequence:
   1. Lookup
   2. Schedule
   3. Remind

---

## 10. Integrate Knowledge Sources
1. **Knowledge** tab:
   - Add **Dataverse**: Tables `Patient`, `Appointment`, `Medication`.
   - Add **SharePoint** library: `KnowledgeDocs`.
2. Configure search filters and indexing.

---

## 11. Test & Publish
1. In **Test** pane, run sample utterances.
2. Debug errors, inspect logs.
3. Click **Publish** in top-right.

---

## 12. Monitor & Maintain
1. Enable **Telemetry** in project settings.
2. Use **Analytics** for usage metrics.
3. Update topics and retrain periodically.

---

*End of guide. Follow each UI instruction exactly to build your Healthcare Copilot agent end-to-end.*