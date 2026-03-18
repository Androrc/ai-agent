# AI Agent CLI (Prototype)

A command-line AI agent prototype using **Google Gemini API**.  
Currently, it accepts text prompts from the user and returns AI-generated responses.  

This project is designed to **explore how LLMs can interact with code**, experiment with **feedback loops**, and understand **agentic coding workflows**.  

## 🚀 Project Goal

- Learn how LLMs can be used for code analysis and reasoning.
- Prototype CLI interactions for reading files and processing prompts.
- Practice iterative improvement of AI-driven code tools.

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