# AI Agent CLI 

A command-line AI agent using **Google Gemini API**.

Currently, it accepts text prompts from the user and returns AI-generated responses.

This project was built for **learning and experimentation purposes**, inspired by modern agentic coding tools such as Cursor, Claude Code, and Zed Agent Mode.

---

## ⚠️ Security Warning

This project is a **toy / educational AI agent** and is **NOT production-ready**.

It does **not** implement the security, sandboxing, permission systems, or safety guarantees expected from real-world AI agents.

The current implementation may expose risks if given access to:
- sensitive files,
- private repositories,
- system commands,
- API keys,
- or unrestricted environments.

Even commercial AI coding agents are not perfectly secure.  
Use this project carefully and **do not deploy or use it as-is in production environments**.

This repository exists purely to explore:
- LLM tool usage,
- feedback loops,
- agent workflows,
- and AI-assisted coding concepts.

---

## 🚀 Project Goal

- Learn how LLMs can be used for code analysis and reasoning.
- Prototype CLI interactions for reading files and processing prompts.
- Practice iterative improvement of AI-driven code tools.

---

## 🛠 Current Features

- Send user prompts to the Gemini API and receive responses.
- Verbose mode to show token usage and prompt/response details.
- Experimental file reading with safe directory traversal checks (`get_files_info`).

## 💻 Installation

1. Clone the repository and install dependencies:

```bash
git clone https://github.com/Androrc/ai-agent.git
cd ai-agent
python -m pip install -r requirements.txt
```
2. Create a .env file with your Gemini API key:

```bash
GEMINI_API_KEY=your_api_key_here
```
3. Run the CLI agent:

```bash
python -m ai_agent.cli "Your prompt here"
```