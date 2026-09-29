# Assignment 24: Ollama Chatbot & LangSmith Tracking

**Student:** Parth Dadhaniya  
**Course:** Generative AI Engineering  

---

## Overview

This assignment covers building a local chatbot using open-source LLMs with Ollama and tracking model responses using LangSmith.

Key objectives:
1. Setup Ollama locally and pull a model (e.g. `llama3`, `mistral`).
2. Invoke the local LLM using LangChain's Ollama wrapper.
3. Build a multi-turn chatbot that remembers conversation history.
4. Track model responses and latency with LangSmith.
5. Create a simple Streamlit interface.
6. Attach a screenshot of the LangSmith dashboard in Google Drive.

---

## Project Files

- `config.py`: Configuration for Ollama URL and LangSmith project credentials.
- `task1_ollama_basic.py`: Task 1 script for connecting to Ollama and sending a basic prompt.
- `task2_ollama_chatbot.py`: Task 2 script demonstrating a multi-turn conversation with memory.
- `task3_langsmith_tracking.py`: Task 3 script demonstrating response tracking in LangSmith.
- `app.py`: Streamlit web app for the Ollama chatbot.
- `main.py`: Master runner that executes all three task scripts in order.
- `assignment24.ipynb`: Jupyter Notebook covering all assignment tasks.
- `requirements.txt`: Python package requirements.
- `README.md`: Assignment documentation and submission details.

---

## Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Ollama Local Setup
1. Download Ollama from https://ollama.com and install it.
2. Open a terminal and start the server:
   ```bash
   ollama serve
   ```
3. Pull the llama3 model:
   ```bash
   ollama pull llama3
   ```
4. Verify by opening `http://localhost:11434` in your browser.

### 3. LangSmith Setup
1. Create a free account at https://smith.langchain.com
2. Get your API key from Settings.
3. Set your environment variables:
   - On Windows (PowerShell):
     ```powershell
     $env:LANGCHAIN_TRACING_V2="true"
     $env:LANGCHAIN_API_KEY="your_api_key_here"
     $env:LANGCHAIN_PROJECT="ollama-chatbot-assignment24"
     ```
   - On Linux/Mac:
     ```bash
     export LANGCHAIN_TRACING_V2="true"
     export LANGCHAIN_API_KEY="your_api_key_here"
     export LANGCHAIN_PROJECT="ollama-chatbot-assignment24"
     ```

*Note: If Ollama or LangSmith are offline, all scripts include built-in simulated responses so they run without errors.*

---

## Running the Code

- Run all tasks together:
  ```bash
  python main.py
  ```
- Run individual tasks:
  ```bash
  python task1_ollama_basic.py
  python task2_ollama_chatbot.py
  python task3_langsmith_tracking.py
  ```
- Launch the Streamlit chatbot:
  ```bash
  streamlit run app.py
  ```

---

## LangSmith Tracking & Drive Screenshot

### How to take the screenshot:
1. Go to https://smith.langchain.com and open the project `ollama-chatbot-assignment24`.
2. Click on the latest run in the list (`ollama_chat_trace`).
3. Make sure the side panel shows the prompt input, model output, and latency.
4. Take a screenshot and save it as `langsmith_screenshot.png`.

### Google Drive Link:
1. Upload the screenshot to Google Drive.
2. Right click -> Share -> Change access to **"Anyone with the link can view"**.
3. Copy and paste the link below:

```
Google Drive Link:
https://drive.google.com/file/d/your-screenshot-id/view?usp=sharing
```
