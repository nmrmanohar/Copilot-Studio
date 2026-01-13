**Demo: “Invoice Processor” agent (Computer use + hosted browser)**

**What this demo does**

Your agent will:

	1. Open the **Contoso Invoice Manager** demo site
	
	2. Filter invoices to **Last 24 hours**
	
	3. Open an invoice PDF
	
	4. Open a second demo site (**invoice submission form**)
	
	5. Copy the data from the PDF into the form
	
	6. **Submit** the invoice form (no confirmation)
	
**Note: These exact sample URLs and instructions come from the Computer use Learn article.** 

**Part 0 — Prerequisites you must set (admin steps)**

**0.1 Create (or use) a United States environment**

Computer use is available only when the **environment region is United States**. 

	1. Go to **Power Platform admin center**. 
      https://aka.ms/ppac
	  
      <img width="1291" height="723" alt="image" src="https://github.com/user-attachments/assets/a3833047-9427-47be-9f2c-98496e3d47f3" />

  2. Left nav: **Manage → Environments**.
	3. Select **New**.
  <img width="1910" height="960" alt="image" src="https://github.com/user-attachments/assets/31b81127-af6c-4e0b-89c9-23d44624f4cb" />

	4. Fill the new environment form exactly like this: 
		○ **Name:** CUA Demo/ any name you prefer
		○ **Region:** United States
		○ **Get new features early:** Yes
		○ **Type:** Sandbox/ Developer (based on your license)
		○ **Add a Dataverse data store:** Yes
	5. Select **Next.**
  <img width="282" height="961" alt="image" src="https://github.com/user-attachments/assets/79766c3c-2729-40d1-b376-b7ac42c521d2" />

	6. On the Dataverse page:
		○ **Language:** English
		○ **Currency:** USD
	7. Select **Save.** 
  <img width="302" height="986" alt="image" src="https://github.com/user-attachments/assets/a700d389-df72-4575-8fd5-6c9b31d591dd" />

**0.2 Ensure “Hosted browser in computer use” is enabled (tenant setting)**
This demo uses **Hosted browser** (Windows 365 managed). 
	1. In **Power Platform admin center**, left nav: Manage → Tenant settings.
	2. Select **Hosted browser in computer use.**
  <img width="1887" height="557" alt="image" src="https://github.com/user-attachments/assets/21506ac1-7dcf-4eaf-b72d-753899c4c614" />

	3. Set the toggle to **On**.
	4. Select **Save**. 
  <img width="311" height="987" alt="image" src="https://github.com/user-attachments/assets/92e0a8f7-0ba9-4f69-a942-acb1ba494aff" />

**0.3 Ensure Computer use is enabled in the environment + enable advanced logging**
	1. In **Power Platform admin center**, left nav: **Manage → Environments**.
	2. Open **environment**: **CUA Demo**
	3. Top menu: **Settings**
  <img width="1235" height="227" alt="image" src="https://github.com/user-attachments/assets/2e38213a-79c0-4e2d-95b0-6b4d13483681" />

	4. Expand **Product** → select **Features**
	5. Scroll to **Computer use** and make sure it is **On** (not disabled). 
Now configure logging (same Features area):
6) Scroll to **Computer Use** settings
7) Set Store logs in Dataverse = On (default). 
8) Set Computer use logs verbosity level = All data (default) 
9) Set Log retention time = 7 days (10,080 minutes) 
<img width="995" height="697" alt="image" src="https://github.com/user-attachments/assets/860d44e0-2358-4747-ba22-263249a5a182" />

**Part 1 — Create the agent (Copilot Studio)**
**1.1 Create agent**
	1. Open **Microsoft Copilot Studio.**
  https://copilotstudio.microsoft.com
  a. If prompted, choose United States in the Country and click **Get Started.**
	2. Select the **environment picker** and choose: CUA Demo/ Your Environment.
  <img width="405" height="432" alt="image" src="https://github.com/user-attachments/assets/cec380d6-e480-4863-952a-8e98702b4121" />

  a.Note, if you are not able to find Environment Selector, **Go to Power Platform Admin Center--> Manage--> Environments--> Select The Environment--> Copy EnvironmentID**
  <img width="1241" height="493" alt="image" src="https://github.com/user-attachments/assets/191c1475-285b-43c0-8686-4ce4f2847716" />
  b. Go to Webbrowser, paste the URL and replace** **<EnvironmentID>**** with the value copied from previous step
  https://copilotstudio.microsoft.com/environments/**<EnvironmentID>**
  <img width="717" height="86" alt="image" src="https://github.com/user-attachments/assets/1dd93da2-df81-4f17-9a38-bbd877b29e4f" />

	3. **Select Agents --> Create blank agent**
  Once the agent is created, follow the next steps
	4. Edit Name: **Contoso Invoice Processor**
  <img width="887" height="183" alt="image" src="https://github.com/user-attachments/assets/a6197dec-646c-4f2b-b846-5209d100ba8f" />

	****1.2 **Enable generative orchestrator** (required)****
Computer use requires the agent to have generative orchestrator enabled. 
	1. In the **agent, select Settings**.
	2. Select Generative AI.
	3. Under Orchestration, set Use generative AI orchestration for your agent’s responses? = **Yes**. 
<img width="1442" height="190" alt="image" src="https://github.com/user-attachments/assets/b1636ef8-9d90-47a3-a263-7f846ca883e5" />

**Part 2 — Add the Computer use tool (the core of the demo)**
**2.1 Add the tool**
	1. In your agent top menu options, select **Tools**.
	2. Select Add tool. 
  <img width="1193" height="163" alt="image" src="https://github.com/user-attachments/assets/8ef32ef7-e0bb-453c-9e5c-97ba778571b4" />

	3. In the dialog, select **New tool**. 
  <img width="902" height="350" alt="image" src="https://github.com/user-attachments/assets/5ae2a340-c49f-4510-bc4b-3779ffca200f" />

	4. Select **Computer use**. 
  <img width="932" height="471" alt="image" src="https://github.com/user-attachments/assets/3d42c9a8-936e-4039-ba87-d5ca4c9e6385" />
  5. Select **Add and configure**.
 
**2.2 Configure Name, Description, and Instructions (paste exactly)**
On the configuration page fill these three fields (required fields). 
**Name**
Invoice processing - hosted browser
**Description**
Opens the Contoso invoice manager demo, opens the latest invoice PDF, copies the invoice details into the invoice submission form, and submits the form.
**Instructions**
Paste exactly (this is the sample “Invoice processing” scenario): 
	1. Go to https://computerusedemos.blob.core.windows.net/web/Contoso/invoice-manager.html, set the Date filter to Last 24 hours, and open the invoice PDF.
	2. In a new tab, open https://computerusedemos.blob.core.windows.net/web/Contoso/index.html and fill out the form with the data from that PDF. Submit the invoice form,no need to add line items, no confirmation needed.
  <img width="1125" height="548" alt="image" src="https://github.com/user-attachments/assets/236cc42d-8412-4527-a145-6e15a80fb2c2" />

**2.3 Choose the machine for runs**
	1. On the tool setup page, for Machine where computer use runs, select Hosted browser.   
**2.4 Set Credentials to use (keep the default)**
	1. In the same tool configuration page, use your current Credentials preferably.
	2. Select **Maker-provided credentials** (default). 
  <img width="742" height="353" alt="image" src="https://github.com/user-attachments/assets/bdbb38cd-2e83-423e-bf42-00d7a3f13161" />

**2.5 Configure Human supervision** (do this for the demo)
The tool supports Human supervision escalation via email when the model detects potentially harmful instructions. 
	1. In tool configuration, find **Human supervision.**
	2. In Reviewer email, enter your **own work email** (the same user running the test). 
	3. Set ** Response time limit = 30 minutes**. (you can set it to 15 minutes if needed)
  <img width="993" height="390" alt="image" src="https://github.com/user-attachments/assets/88e5cd33-551a-407e-9f10-534d88c5b5e1" />

**2.6 Lock down the tool with Access control (do this)**
By default computer use can act on any website/app; you should restrict it. 
	1. In tool configuration, find **Access control.**
	2. Set **Access control = On.**
	3. Under Websites allowlist, add this entry:
		**○ computerusedemos.blob.core.windows.net **
    <img width="1032" height="791" alt="image" src="https://github.com/user-attachments/assets/63ce8033-1cbb-4315-b8e6-4cc4083ff1fc" />

**2.7 Save the tool**
	1. Select **Save**. 

**Part 3 — Test the Computer use tool (inside the tool test harness)**
**3.1 Run the built-in tool test**
The Learn page explicitly recommends testing via the Test experience in the tool configuration. 
	1. While still on the tool configuration page, **select Test.**
  <img width="1078" height="435" alt="image" src="https://github.com/user-attachments/assets/ca42ba87-9ae9-4234-9451-c26cbdd01a28" />

	2. Wait for the tool test UI to load.
	3. **Watch the test run:**
		○ Left panel shows instructions + step-by-step log of reasoning/actions
		○ Right panel shows the hosted browser performing clicks/typing 
	4. When you see Test completed, select Close. 
	**If the test fails with a “no machine found” / hosted browser availability issue, it can happen due to throttling or an already-active hosted browser session (one active session per user). Wait for 15 minutes and try again**
<img width="977" height="465" alt="image" src="https://github.com/user-attachments/assets/58bf30c6-732f-44e7-a1d8-f276eb580ff8" />

**Part 4 — Make it a conversational demo (user asks, agent runs tool)**
**4.1 Add main agent instructions so orchestration always uses the tool**
	1. Go to the agent Overview.
	2. In **Instructions**, paste this block at the end:

When the user asks to “process an invoice” or “submit the latest invoice”, run the tool “Invoice processing - hosted browser”.
After the tool finishes, summarize the result in 2 sentences and include whether the invoice was submitted.
<img width="1075" height="737" alt="image" src="https://github.com/user-attachments/assets/716a9654-8b76-4c8f-967d-0081398ae92e" />

This aligns with “computer use works best for autonomous/background runs” but can be used in conversational experiences too. 
**4.2 Test in the agent chat**
	1. Open the agent’s Test chat.
	2. Type exactly:
**Process the latest invoice using the demo sites and submit it.**
	3. Confirm the agent runs the computer use tool and you see the tool’s screenshots/reasoning surfaced during execution (expected behavior in conversational runs). 

**Part 5 — Show monitoring (this is the “enterprise proof” moment)**
**5.1 Open Activities and inspect the run**
	1. In Copilot Studio, open your agent.
	2. Go to **Activities**.
	3. Open the most recent run.
	4. Select the **computer use** action in the **activity map** to open the side panel.
You should see details like session replay (screenshots), activity timestamps, websites accessed, credentials used, and export options. 


What this demo proves (in plain terms)
	• You can add Computer use as a tool (Tools → Add tool → New tool → Computer use). 
	• You can run it on Hosted browser (Windows 365 managed) without machine setup. 
	• You can secure it with Access control allowlists and Human supervision. 
	


