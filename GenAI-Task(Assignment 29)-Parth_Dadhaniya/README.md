# Assignment 29: Q&A Chatbot Application (OpenAI & Ollama)

**Student:** Parth Dadhaniya  
**Course:** GenAI - TuteDude  

---

## Overview

In real-world enterprise applications, Generative AI Engineers frequently choose between closed-source cloud APIs (like OpenAI) and local, open-source models (like Ollama running Llama 3). 

In this assignment, I built:
1. **OpenAI Q&A Chatbot**: A cloud-based conversational assistant using `ChatPromptTemplate` tested across 5 diverse technical questions, with multi-turn context retention.
2. **Ollama Q&A Chatbot**: A local, privacy-first open-source chatbot using `llama3` running on an offline machine.
3. **Model Switcher**: A unified interface (`get_answer(question, model_type)`) allowing switching between OpenAI and Ollama.
4. **Interactive Chat Interfaces**: A terminal CLI mode and an interactive Streamlit web UI.
5. **Comprehensive Comparison**: Analysis across response quality, latency, cost, and privacy.

---

## File Structure

```text
GenAI-Task(Assignment 29)-Parth_Dadhaniya/
├── config.py                 # OpenAI and Ollama model wrappers & health checks
├── part1_openai_chatbot.py   # Part 1: OpenAI setup, 5-question test & multi-turn Q&A
├── part2_ollama_chatbot.py   # Part 2: Ollama setup, local execution & model comparison
├── part3_unified_app.py      # Part 3: Model switch logic (get_answer) & interactive CLI
├── streamlit_app.py          # Part 3: Streamlit web interface with model switcher
├── task9_observations.py     # Part 4: Analytical observations & trade-offs
├── main.py                   # Master script running all tasks
├── assignment29.ipynb        # Interactive Jupyter Notebook
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
```

---

## Tasks Summary

### Part 1: Q&A Chatbot using OpenAI (Tasks 1, 2, 3)
- Configured OpenAI chat integration using `ChatPromptTemplate` (System message + Human message).
- Tested across 5 diverse technical questions:
  1. *Supervised vs Unsupervised learning*
  2. *Python decorators*
  3. *Overfitting prevention*
  4. *Web APIs*
  5. *Vector databases*
- Demonstrated multi-turn dialog context retention with follow-up queries.

### Part 2: Q&A Chatbot using Ollama (Tasks 4, 5, 6)
- Checked local Ollama server connectivity (`http://localhost:11434`) and verified `llama3`.
- Executed local queries using identical prompt templates.
- Compared OpenAI and Ollama across response quality, latency, token costs, and privacy.

### Part 3: Unified App & Model Switch Logic (Tasks 7 & 8)
- Implemented `get_answer(question, model_type="openai")` supporting dynamic switching between OpenAI and Ollama.
- Built an interactive CLI (`--interactive`) and a clean Streamlit chat application (`streamlit_app.py`).

### Part 4: Observations & Conceptual Insights (Task 9)
- Analyzed enterprise trade-offs between pay-per-token cloud services and dedicated open-source GPU deployments.

---

## How to Run

### Run All Tasks (Master Script)
```bash
python main.py
```

### Run Individual Parts
```bash
python part1_openai_chatbot.py
python part2_ollama_chatbot.py
python part3_unified_app.py
python task9_observations.py
```

### Interactive Terminal CLI
```bash
python part3_unified_app.py --interactive
```

### Launch Streamlit Web UI
```bash
streamlit run streamlit_app.py
```
