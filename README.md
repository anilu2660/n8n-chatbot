# 🤖 AI Personal Assistant — Powered by n8n Agent Workflow

An intelligent, multi-functional personal assistant chatbot built with **Streamlit** and **n8n Agent Workflow**. This assistant connects to Google services (Gmail, Calendar, Tasks, Docs, Sheets) via n8n automation to help you manage your daily tasks through a simple chat interface.

![Python](https://img.shields.io/badge/Python-3.12+-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?logo=streamlit&logoColor=white)
![n8n](https://img.shields.io/badge/n8n-Agent%20Workflow-EA4B71?logo=n8n&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

---

## ✨ Features

| Feature | Description | Google Service |
|---------|-------------|----------------|
| 💬 **Q&A** | Answer general knowledge and factual questions | Google Search |
| 📅 **Calendar Management** | Create events, fetch schedules, view upcoming meetings | Google Calendar |
| 📧 **Email Management** | Read, summarize, and reply to emails | Gmail |
| ✅ **Task Management** | Create, view, and delete tasks and to-do items | Google Tasks |
| 📝 **Notes** | Create, update, and read notes | Google Docs |
| 💰 **Expense Tracking** | Log expenses, view history, calculate budgets | Google Sheets |

---

## 🏗️ Architecture

```
┌─────────────────────┐         ┌──────────────────────────────────┐
│                     │  HTTP   │                                  │
│  Streamlit Frontend │ ──────► │  n8n Agent Workflow (Cloud)      │
│  (app.py)           │  POST   │                                  │
│                     │ ◄────── │  ┌─────────────┐                 │
└─────────────────────┘  JSON   │  │  AI Agent    │                 │
                                │  │  (LLM +      │                 │
                                │  │   Tools)     │                 │
                                │  └──────┬───────┘                 │
                                │         │                         │
                                │  ┌──────▼───────────────────┐     │
                                │  │  Tool Nodes               │    │
                                │  │  • Google Calendar         │    │
                                │  │  • Gmail                   │    │
                                │  │  • Google Tasks            │    │
                                │  │  • Google Docs             │    │
                                │  │  • Google Sheets           │    │
                                │  │  • Google Search            │   │
                                │  │  • Calculator              │    │
                                │  └────────────────────────────┘   │
                                └──────────────────────────────────┘
```

### How It Works

1. **User** types a message in the Streamlit chat interface.
2. The message is sent as a **POST request** to the n8n webhook endpoint.
3. **n8n Agent Workflow** receives the message and processes it through an **AI Agent node** powered by an LLM.
4. The AI Agent analyzes the user's intent and selects the appropriate **tool** (Gmail, Calendar, Tasks, etc.).
5. The tool executes the action via Google APIs and returns the result.
6. The response is sent back to the Streamlit app and displayed to the user.

---

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/) — Python-based interactive web UI
- **Backend / Automation**: [n8n](https://n8n.io/) — Workflow automation platform with AI Agent capabilities
- **AI Agent**: n8n AI Agent node with LLM-powered decision making
- **Integrations**: Google Calendar, Gmail, Google Tasks, Google Docs, Google Sheets, Google Search
- **Language**: Python 3.12+
- **Package Manager**: [uv](https://docs.astral.sh/uv/) (fast Python package manager)

---

## 📁 Project Structure

```
n8n-chatbot/
├── app.py               # Main Streamlit application (chat UI + webhook integration)
├── main.py              # Basic entry point script
├── sysprompt.md         # System prompt for the n8n AI Agent
├── test_webhook.py      # Webhook testing utility script
├── pyproject.toml       # Project metadata and dependencies
├── .python-version      # Python version specification (3.12)
├── .gitignore           # Git ignore rules
├── uv.lock              # Dependency lock file
└── README.md            # Project documentation
```

### Key Files

| File | Purpose |
|------|---------|
| `app.py` | The main application — Streamlit chat interface that sends user messages to the n8n webhook and displays AI responses |
| `sysprompt.md` | Detailed system prompt defining the AI Agent's role, capabilities, available tools, decision-making guidelines, and response style |
| `test_webhook.py` | A standalone script for testing the n8n webhook endpoint independently |

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.12+** installed
- **uv** package manager ([install guide](https://docs.astral.sh/uv/getting-started/installation/))
- An active **n8n cloud account** (or self-hosted n8n instance) with the Agent workflow set up
- **Google Cloud** credentials configured in n8n for Calendar, Gmail, Tasks, Docs, and Sheets

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/anilu2660/n8n-chatbot.git
   cd n8n-chatbot
   ```

2. **Install dependencies using uv**
   ```bash
   uv sync
   ```

3. **Update the webhook URL** (if using your own n8n instance)

   Open `app.py` and update the webhook URL on **line 45** with your own n8n webhook URL:
   ```python
   response = requests.post(
       "https://your-n8n-instance.app.n8n.cloud/webhook/your-webhook-id",
       json={"message": user_message}
   )
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. Open your browser and navigate to `http://localhost:8501`

---

## ⚙️ n8n Workflow Setup

To set up the n8n Agent Workflow on your end:

1. **Create a new workflow** in your n8n dashboard.
2. **Add a Webhook node** as the trigger:
   - Method: `POST`
   - Response: `Respond to Webhook`
3. **Add an AI Agent node** connected to the webhook:
   - Configure the LLM (e.g., OpenAI GPT-4, Google Gemini, etc.)
   - Paste the contents of `sysprompt.md` as the system prompt
4. **Add Tool nodes** for each integration:
   - 🔍 Google Search
   - 📅 Google Calendar (Create Event, Get Event, Get Events)
   - 📧 Gmail (Get Messages, Get Single Message, Send Message)
   - ✅ Google Tasks (Create, Get Single, Get Multiple, Delete)
   - 📝 Google Docs (Create, Update, Get Notes)
   - 💰 Google Sheets (Add Expense, Get Expenses)
   - 🧮 Calculator
5. **Connect** all tool nodes to the AI Agent.
6. **Activate** the workflow.
7. Copy the **production webhook URL** and paste it in `app.py`.

---

## N8N Workflow :
<img width="1608" height="697" alt="image" src="https://github.com/user-attachments/assets/4391f2e5-fb00-4e46-b260-fdfdb947306d" />
This is the picture of n8n workflow how it handles the prompt


## 💬 Usage Examples

Here are some things you can say to your assistant:

| Category | Example Prompt |
|----------|---------------|
| 📧 Email | *"Summarize my last 3 emails"* |
| 📧 Email | *"Reply to the email from John saying I'll be there at 5 PM"* |
| 📅 Calendar | *"Create a meeting with the team tomorrow at 3 PM"* |
| 📅 Calendar | *"What meetings do I have this week?"* |
| ✅ Tasks | *"Add a task: Complete project report by Friday"* |
| ✅ Tasks | *"Show me all my pending tasks"* |
| 📝 Notes | *"Take a note: Ideas for the new marketing campaign"* |
| 💰 Expenses | *"Add an expense: ₹500 for lunch"* |
| 💰 Expenses | *"What's my total spending this month?"* |
| 💬 General | *"What's the weather in New York?"* |

---

## 🧪 Testing

Use the included `test_webhook.py` script to test the n8n webhook independently:

```bash
python test_webhook.py
```

This will send a test message to the webhook and print the raw response, helping you verify that your n8n workflow is active and responding correctly.

---

## 🔧 Configuration

| Setting | Location | Description |
|---------|----------|-------------|
| Webhook URL | `app.py` (line 45) | Production n8n webhook endpoint |
| Test Webhook URL | `test_webhook.py` (line 8) | Test webhook endpoint for debugging |
| System Prompt | `sysprompt.md` | AI Agent behavior and tool usage rules |
| Python Version | `.python-version` | Required Python version (3.12) |

---

## 📦 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `streamlit` | ≥ 1.53.0 | Web-based chat interface |
| `requests` | (built-in via streamlit) | HTTP requests to n8n webhook |

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙏 Acknowledgments

- [n8n](https://n8n.io/) — For the powerful workflow automation and AI Agent capabilities
- [Streamlit](https://streamlit.io/) — For the simple and elegant Python web framework
- Google Cloud APIs — For Calendar, Gmail, Tasks, Docs, and Sheets integrations

---

<p align="center">
  Built with ❤️ using <strong>n8n Agent Workflow</strong> and <strong>Streamlit</strong>
</p>
