# 🧠 LangGraph Experiments

This repository contains a collection of modular experiments and examples exploring the capabilities of [LangGraph](https://docs.langchain.com/langgraph/), a powerful framework for building agentic workflows using graphs. The focus is on state management, agent reasoning, tool use, and advanced multi-agent orchestration.

---

## 📁 Directory Overview

```
1_introduction/
  └── react_agent_basic.py       # Minimal React-style agent setup

2_basic_reflection_system/
  ├── basic.py                   # Entry reflection logic
  ├── chains.py                  # Modular reflection chains

3_structured_outputs/
  └── types.py                   # Pydantic schemas and output typing

4_reflexion_agent_system/
  ├── chains.py
  ├── execute_tools.py           # Tool routing logic
  ├── reflexion_graph.py         # Main agent graph with reflexion loop
  └── schema.py                  # Structured reflection format

5_state_deepdive/
  ├── 1_basic_state.py           # Simple state handling
  └── 2_complex_state.py         # Multi-slot state with metadata

6_react_agent/
  ├── agent_reason_runnable.py
  ├── nodes.py
  ├── react_graph.py             # Full React agent implementation
  └── react_state.py

7_chatbot/
  ├── 1_basic_chatbot.py
  ├── 2_chatbots_with_tools.py   # Tool-enabled dual chatbot agents
  ├── 3_chatbot_with_in_memory_checkpointer.py
  └── 4_chat_with_sqlite_checkpointer.py

8_human-in-the-loop/
  ├── 1_using_input().py         # Manual input capture
  ├── 2_command.ipynb
  ├── 3_resume.ipynb
  ├── 4_approval-pending.ipynb
  └── 5_multiturn_conversation-pending.py

9_RAG_agent/
  ├── 2_classification_driven_agent.ipynb
  └── 3_rag_powered_tool_calling.ipynb

10_multiagent_architecture/
  └── 1_subgraphs.ipynb          # Subgraph orchestration
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/langgraph-lab.git
cd langgraph-lab
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # or `.env\Scriptsctivate` on Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

You may also need:

```bash
pip install langgraph langchain langchain-community langchain-groq python-dotenv
```

---

## 🧪 Usage

Each folder is self-contained and can be run independently. Start with:

```bash
python 1_introduction/react_agent_basic.py
```

Or explore more complex agents like:

```bash
python 6_react_agent/react_graph.py
```

---

## 🛠️ Features Demonstrated

- ✅ React and Reflexion Agent Patterns
- 🔄 LangGraph State Management
- 🧰 Tool Integration (e.g. Tavily Search)
- 🧠 LLM Reasoning Loops
- 🧱 Modular Graph Nodes & Subgraphs
- 🧾 Structured Outputs using Pydantic
- 🧑‍🏫 Human-in-the-loop Workflows
- 🔎 RAG (Retrieval Augmented Generation)

---

## 🧠 Credits

Built using:
- [LangGraph](https://docs.langchain.com/langgraph/)
- [LangChain](https://www.langchain.com/)
- [Groq LLMs](https://groq.com/)
- [Tavily Search Tool](https://www.tavily.com/)

---

## 📬 Contact

Feel free to reach out for questions, collaborations, or contributions!