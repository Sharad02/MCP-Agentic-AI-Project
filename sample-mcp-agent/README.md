# 🧠 Sample MCP Agentic AI Project

This project demonstrates how to connect an **Agentic AI (Gemini / OpenAI)** with a **Monetary Control Platform (MCP)** using structured financial data. It's a beginner-friendly setup to simulate Fi MCP architecture and learn how AI agents can reason over real user data.

---

## 🔧 Tech Stack

| Tool            | Purpose                             |
|-----------------|-------------------------------------|
| Python          | Main language                       |
| OpenAI / Gemini | LLM agent interface                 |
| MCP (JSON)      | Structured user financial data      |
| Streamlit       | Optional frontend UI                |
| GitHub          | Version control and publishing      |

---

## ⚙️ Architecture Overview
User → [Frontend UI] → [LLM Agent] → [Agent Toolset]
↘ ↓
[MCP (Fi API or Mock)] ←→ [Structured Financial JSON]

The LLM agent receives queries like "What’s my net worth?" and uses tools to fetch & compute values from MCP data.

---

## 📁 Project Structure

sample-mcp-agent/
├── agent.py # Main agent logic
├── mcp_connector.py # (Placeholder) API/MCP connector
├── frontend_app.py # (Optional) Streamlit UI
├── prompts/
│ └── planner_prompt.txt # Sample prompt for agent planning
├── test_data/
│ └── sample_mcp.json # Mock user data
├── requirements.txt # Python dependencies
└── README.md


## 💰 Sample Use Case

### ✅ Prompt: _"What is my net worth?"_

**🧠 Agent Logic:**
- Fetch asset and liability data
- Compute: `Net Worth = Total Assets - Total Liabilities`
- Respond naturally

**🔢 Example Output:**
Your net worth is ₹110000

---

## 🧪 Sample MCP Data (`test_data/sample_mcp.json`)

```json
{
  "user": "Sharad",
  "assets": {
    "bank": 60000,
    "stocks": 80000,
    "crypto": 10000
  },
  "liabilities": {
    "loan": 40000
  },
  "credit_score": 750
}
🚀 How to Run

# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the agent script
python agent.py
📦 Future Add-Ons
🔐 Integrate with real MCP API

🧠 Add more queries: "What’s my credit score?", "How much do I owe?"




