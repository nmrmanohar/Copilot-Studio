 **“Connect to an existing Copilot Studio agent.” **
You will build 3 agents in the same environment:
	• **Main agent: Contoso Orchestrator
	• Connected agent 1: Approvals Specialist
	• Connected agent 2: IT Password Reset Specialist**
The main agent will connect to the two specialist agents and then route to them from a topic (and also be able to pick them via generative orchestration).

**Prerequisites** (must be true for this demo)
	1. Both specialist agents must be Published before the main agent can connect to them.   
	2. Both specialist agents must be configured to allow connections from other agents (toggle in Settings). 
	4. If you’re using a trial license, note: you can test agents but you can’t publish, which will block the “connect existing agent” requirement. 

Knowledge sources to incorporate (add these exact URLs)
You will add one knowledge source to each specialist agent:
	**• Approvals Specialist knowledge source:**
  https://learn.microsoft.com/en-us/microsoft-copilot-studio
Note: We will try to get answers related to Approvals (https://learn.microsoft.com/en-us/microsoft-copilot-studio/flows-advanced-approvals)
	**• Password Reset Specialist knowledge source:**
  https://learn.microsoft.com/en-us/microsoft-365
Note: We will try to get answers related to Password Reset (https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/reset-passwords?view=o365-worldwide)
**And (optional but recommended) add Power Platform docs to the main orchestrator:**
  https://learn.microsoft.com/en-us/power-platform/
	
**Part A — Build and publish the specialist agents**
**A1) Create agent: “Approvals Specialist”**
	1. Open Microsoft Copilot Studio.
	2. Select **Agents → Create blank agent.**
	3. Once created, Set Name to: **Approvals Specialist**
	<img width="1057" height="352" alt="image" src="https://github.com/user-attachments/assets/d0616d28-9303-43ef-874c-fc6257d275eb" />

Add knowledge source
	5. On the agent Overview page, go to Knowledge.
	6. Select **Add knowledge**. 
  <img width="864" height="63" alt="image" src="https://github.com/user-attachments/assets/38551ded-27c0-4975-b67e-bb5e5cb5a67f" />

	7. Select Public websites.
  <img width="939" height="597" alt="image" src="https://github.com/user-attachments/assets/89fd3b7e-6163-449b-ad9f-0c6019c1d7cb" />

	8. In the URL box, paste:
https://learn.microsoft.com/en-us/microsoft-copilot-studio
	9. Select Add.
  <img width="912" height="222" alt="image" src="https://github.com/user-attachments/assets/5372db72-2557-4327-bfc2-ff5b57493618" />

	10. Select Add to agent. 
  <img width="976" height="658" alt="image" src="https://github.com/user-attachments/assets/aef0169d-f32a-4e2b-b3f2-363f6425be42" />

**Set agent instructions (make it clearly specialized)**
	11. In **Instructions** under agent Overview, paste exactly:

You are the Approvals Specialist.
You answer only questions about multi-stage approvals and AI/manual approval stages in Copilot Studio agent flows.
Use the connected knowledge source as the authority.
If a question is about password reset or sign-in, state “This is IT/password reset” and stop.
Return short, step-by-step guidance.
<img width="1102" height="795" alt="image" src="https://github.com/user-attachments/assets/cf46943e-d11e-421c-86a1-138457aee2c3" />

**Allow connections from other agents (required)**
	12. Go to **Settings** for this agent.
  <img width="1842" height="248" alt="image" src="https://github.com/user-attachments/assets/7ac422cb-deb2-4771-93e4-4d5d3f193559" />

	13. **Turn On: Let other agents connect to and use this one.** , Save, close the settings page.
  <img width="1855" height="918" alt="image" src="https://github.com/user-attachments/assets/ec9db069-89bb-46fb-a425-a668869bc0ec" />

**Publish (required so other agents can use the latest version)**
	14. At the top in the age, select** Publish.**
  <img width="1766" height="73" alt="image" src="https://github.com/user-attachments/assets/4f8dbeba-0ca0-4965-88b3-edceb3b386aa" />

	15. Select** Publish again** in the confirmation message. 
	**Important: **after any changes, you must publish again; the connecting agent can only use the latest published version. 

**A2) Create agent: “IT Password Reset Specialist”** 
(please follow screens from previous agent if needed)
	1. Select **Agents → Create blank agent.**.
	2. Set Once created, change Name to: **IT Password Reset Specialist**
	
**Add knowledge source**
	4. On **Overview**, go to **Knowledge.**
	5. Select **Add knowledge**. 
	6. Select **Public websites**. 
	7. Paste URL:
https://learn.microsoft.com/en-us/microsoft-365
	8. Select **Add** → **Add to agent**. 
**Set agent instructions**
	9. In Instructions, paste exactly:

You are the IT Password Reset Specialist.
Provide step-by-step guidance for Microsoft 365 password resets using the knowledge source.
If the user is not an admin, explain what they can do and what an admin must do.
If the question is about approvals or Copilot Studio flows, state “This is approvals/flows” and stop.
Keep answers short and procedural.

**Allow connections from other agents (required)**
10. Go to **Settings** for this agent.
11. **Turn On: Let other agents connect to and use this one.** , Save, close the settings page.
**Publish (required so other agents can use the latest version)**
	12. At the top in the age, select** Publish.**
	13. Select** Publish again** in the confirmation message. 
	**Important: **after any changes, you must publish again; the connecting agent can only use the latest published version. 

**Part B — Create the main orchestrator agent and enable generative orchestration**
B1) C**reate main agent: “Contoso Orchestrator”**
	1. Select **Agents → Create blank agent.**.
	2. Set Once created, change Name to: **Contoso Orchestrator**
	
B2) **Turn on generative orchestration (so it can choose other agents)**
	1. Go to **Settings.**
	2. Under **Generative AI** → **Orchestration:**
	3. **Set Use generative AI orchestration for your agent’s responses? to Yes.** 
Generative orchestration allows the agent to choose the best tools, knowledge, topics, and other agents based primarily on their descriptions. 
**B3) Add a knowledge source to the main agent(optional but recommended)**
	1. Go to **Overview**.
	2. In **Knowledge**, select **Add knowledge**.
	3. Select **Public websites**.
	4. Paste: https://learn.microsoft.com/en-us/power-platform/
	5. Select **Add** → **Add to agent.** 

**Part C — Connect the two existing Copilot Studio agents (the key part of this URL)**
**C1) Connect “Approvals Specialist” to the main agent**
	1. **In Contoso Orchestrator, go to Agents.**
	2. Go to **Overview**, **Agents** --> Select **Add an agent**. 
  <img width="1083" height="517" alt="image" src="https://github.com/user-attachments/assets/b6509da6-3f9b-4b87-ac62-9856dddb2ac3" />

	3. Under **Select an agent in your environment**, from the list, select **Approvals Specialist**. (You should see its name, instructions, and description.) 
  <img width="916" height="653" alt="image" src="https://github.com/user-attachments/assets/016279f1-b730-46b1-8d2f-b4329615abca" />

	4. In the **Description** field (the local description used by the main agent), replace it with this exact text:
Use this agent for Copilot Studio multi-stage approvals, AI approvals, manual stages, conditions, and approval flows. Not for password resets.
	5. Leave **Pass conversation history to this agent checked** (ON). 
	6. Select Add / Save (whatever the final action is in your UI to complete the connection).
  <img width="933" height="666" alt="image" src="https://github.com/user-attachments/assets/b6b139d6-67ab-44ed-8d73-3b9ad46ca7f6" />

C2) Connect “IT Password Reset Specialist” to the main agent
	1. Still in **Contoso Orchestrator** → **Agents**, select **Add an agent**. 
	2. Under **Connect to an external agent**, 
	3. Select **IT Password Reset Specialist** from the list. 
	4. Replace its local **Description** with this exact text:
**Use this agent for Microsoft 365 sign-in and password reset guidance. Not for approvals or Copilot Studio flows.**
	5. **Clear the checkbox Pass conversation history to this agent (OFF)**. 
		○ This ensures the main agent passes only the explicit task, limiting what the connected agent receives. 
	6. Select** Add **/ Save to complete the connection.
	Note: once connected, the description is controlled locally in the main agent; changes to the connected agent’s description don’t auto-sync back. 

**Part D — Make orchestration deterministic: create a router topic that explicitly calls the connected agents**
**D1) Create topic “Route to specialist”**
	1. In Contoso Orchestrator, go to** Topics**.
	2. Select + **New topic**, **From Blank**.
  <img width="963" height="193" alt="image" src="https://github.com/user-attachments/assets/19a3340d-e2ea-43f5-98b4-bd0cab1e5a3f" />

	3. Set **Name: Route to specialist**, Save.
  <img width="1192" height="232" alt="image" src="https://github.com/user-attachments/assets/8f7e8fa6-ed5e-4f90-8d63-91d60710a5e1" />

	4. Add Description to the Trigger:
  Request related to 
		○ help desk
		○ support
    ○ Password Reset
		○ Approvals 
    <img width="410" height="271" alt="image" src="https://github.com/user-attachments/assets/adfbfb9e-65e9-441a-9988-536529560090" />

D2) Add the routing question
	5. Under the trigger node, select **Add node (+)**.
	6. Select Ask a question.
  <img width="441" height="622" alt="image" src="https://github.com/user-attachments/assets/c7307d31-decd-4469-ab8e-325edd940d97" />

	7. **Question text**:** Which specialist do you need?**
	8. **Identify**: Multiple choice
	9. Add choices exactly:
		○ Approvals
		○ Password reset
 <img width="331" height="388" alt="image" src="https://github.com/user-attachments/assets/41adeced-f96e-4591-97e4-aa3dce4de90c" />
   
	10. Save response to variable: specialistChoice
  <img width="750" height="768" alt="image" src="https://github.com/user-attachments/assets/2027067f-5cd2-4c48-9dd8-e4874ef852fc" />

**D3) Add a condition**
	11. Select **Add node (+)**. 
  Note: If condition node already shows up, no need to add another
	12. Select Condition.
	13. Configure:
	• If specialistChoice equals Approvals → Approvals branch
	• Else → Password reset branch
  <img width="992" height="387" alt="image" src="https://github.com/user-attachments/assets/c83a3c69-e9ea-462b-9aeb-a1d789e555c3" />

D4) Approvals branch: redirect to connected agent
	14. In the Approvals branch, select Add node (+).
	15. Select Add an agent.
	16. Select the connected agent Approvals Specialist.
  <img width="721" height="632" alt="image" src="https://github.com/user-attachments/assets/46727cbc-728b-4781-bfa8-86c9ff6dc8e5" />

	17. Under that agent node, select Add node (+) add Send a message:
Returned from Approvals Specialist. What else do you need?
<img width="366" height="637" alt="image" src="https://github.com/user-attachments/assets/b612e626-52d6-498f-a162-16a426bf7d2d" />

D5) Password reset branch: redirect to connected agent
	18. In the Password reset branch, select Add node (+).
	19. Select Add an agent.
	20. Select the connected agent IT Password Reset Specialist.
	21. Under that agent node, add Send a message:
Returned from Password Reset Specialist. What else do you need?
	22. Select Save for the topic.

Part E — Test (prove orchestration + connected agent calls)
E1) Test run: approvals route
	1. Open the Test panel.
  <img width="674" height="917" alt="image" src="https://github.com/user-attachments/assets/8bde4a83-043c-4560-92fd-76a3d8501dca" />
	2. Type: help desk
	3. Select: Approvals
  <img width="624" height="836" alt="image" src="https://github.com/user-attachments/assets/f626d4ba-7465-4912-b587-65e4812cebf6" />
See the response and Activity Map on the left screen to show how the process happens
  
E2) Test run: password reset route
	1. Start a new test session.
	2. Type: support
	3. Select: Password reset
  4. or simply type reset password by skipping step 1 and 2.
  <img width="1828" height="761" alt="image" src="https://github.com/user-attachments/assets/2403ad81-3ae6-46de-9470-0048283f72ea" />

E3) Show the activity map (optional but great for demos)
While testing, open the activity map to show how the main agent chose topics/agents and in what order. 

What this demo proves (tie-back to the URL)
	• You connected an existing Copilot Studio agent by going to Agents → Add an agent → Copilot Studio and selecting the target agent. 
	• You ensured prerequisites: same environment, published, and “Let other agents connect…” enabled. 
	• You controlled orchestration quality by updating the connected agent’s local description (critical for correct invocation). 
	• You demonstrated governance of context by turning Pass conversation history ON for one agent and OFF for the other. 
<img width="925" height="4723" alt="image" src="https://github.com/user-attachments/assets/2dec9277-db70-4a5e-a1c8-abde1895f1d5" />
