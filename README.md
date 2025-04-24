# README.md

# 🤖 Adaptive Multi-Agent Research System

**A streamlined AI system powered by adaptive agents that research, analyze, and innovate in sync.**
This project blends dynamic research, analytical insight, and strategic innovation using real-time web data and multi-model language reasoning—presented through an interactive Streamlit interface with local authentication and memory logging.

Project URL: [https://github.com/AhmedMostafaAttiaaa/Adaptive-Multi-Agent-Research-System](https://github.com/AhmedMostafaAttiaaa/Adaptive-Multi-Agent-Research-System)

Follow these steps to install all dependencies and launch the full web-based AI research assistant:

1. **Clone the repository**:
```bash
git clone https://github.com/AhmedMostafaAttiaaa/Adaptive-Multi-Agent-Research-System.git
cd SynapseStack
```

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

3. **Configure environment variables**:
Create a `.env` file:
```env
MY_USERNAME=your_username
MY_PASSWORD=your_password
SERPER_API_KEY=...
GEMINI_API_KEY=...
GROQ_API_KEY=...
OPENROUTER_API_KEY=...
```

4. **Run the app**:
```bash
streamlit run app.py
```

---

## 🛠️ Usage Overview

This system was designed and implemented to explore adaptive multi-agent collaboration using [CrewAI]. Once the user logs in through the Streamlit interface, the system proceeds in three core steps:

1. **Research Phase** – The Research Agent uses tools like Serper and web scraping to collect fresh data related to the user’s topic.
2. **Analysis Phase** – The Analysis Agent processes and interprets this data, surfacing patterns, anomalies, and trends.
3. **Innovation Phase** – The Innovation Agent synthesizes insights into structured Markdown reports with strategic recommendations.

Each step is handled by a dedicated LLM, carefully selected for its strengths:

- 🔷 **Gemini (gemini-2.0-flash)**: Chosen for web research and real-time context adaptation.
- 🔶 **Groq (llama-3.3-70b-versatile)**: Used for deep analytical reasoning and pattern detection.
- 🟣 **OpenRouter (deepseek-chat-v3-0324:free)**: Powers the innovation agent to propose creative directions and structured outputs.

---

## 📄 Codebase Overview

Below is a breakdown of the main Python files and their responsibilities in the project:

- **`agent.py`**: Defines the three core agents (Research, Analysis, Innovation), each with its own goal, LLM, and tools.
- **`task.py`**: Contains functions that generate dynamic `Task` objects for each agent based on the topic and input.
- **`tools.py`**: Includes custom tools such as Serper API-based search, web scraping, file reading, and markdown writing.
- **`llm_config.py`**: Handles API key loading and initializes the three large language models (Gemini, Groq, OpenRouter) used by the agents.
- **`Crewkickoff.py`**: Central orchestration function `run_ai_workflow()` that connects agents and tasks into a Crew and executes them in order.
- **`utils.py`**: Loads environment variables from `.env` and provides helper functions to retrieve API keys securely.
- **`app.py`**: Streamlit web interface that manages login, topic input, execution of the workflow, and rendering of results.

---

## 🖼️ System Architecture Diagram

Below is a visual overview of the Adaptive Multi-Agent Research System flow:

![System Diagram](https://raw.githubusercontent.com/AhmedMostafaAttiaaa/Adaptive-Multi-Agent-Research-System/main/assets/flowchart.png)

---

## 📁 Project Output Files
This repository will include example outputs from the AI agents — such as generated Markdown reports, PDF summaries, and interaction logs.

---

## 🔐 Security Notes
- Never commit `.env` or expose your API keys
- Local-only execution recommended for testing

---

## 🧾 License
MIT License © 2025 — Built by Ahmed Mostafa Attia  
<a href="https://www.linkedin.com/in/ahmed-mostafa-2110341a4/" target="_blank">
  <img src="https://img.shields.io/badge/LinkedIn-Ahmed%20Mostafa-blue?logo=linkedin" alt="LinkedIn badge" />
</a>
