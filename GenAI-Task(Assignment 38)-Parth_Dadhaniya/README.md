# Assignment 38: CodeLlama Developer Assistant using Ollama

**Student:** Parth Dadhaniya  
**Course:** Generative AI Engineering — TuteDude  
**Topic:** Developer-Focused GenAI Applications, CodeLlama Local Inference via Ollama, LangChain Integration, Code Generation, Explanation, Debugging, Optimization, and Streamlit UI  

---

## 📌 Problem Statement & Scenario

Modern Generative AI systems go beyond simple conversational chatbots—they serve as **autonomous software engineering assistants** capable of generating syntactically valid code, explaining complex algorithms, diagnosing and fixing software bugs, and optimizing computational bottlenecks.

In this assignment, we build a local, developer-focused **AI Coding Assistant powered by CodeLlama (via Ollama)** and **LangChain**, featuring:
1. Local setup and model management with Ollama (`codellama:7b`).
2. LangChain integration using specialized prompt engineering templates.
3. Four core engineering capabilities:
   - **Code Generation:** Generating production-ready Python functions with docstrings, type hints, and usage examples.
   - **Code Explanation:** Deconstructing functions into parameters, algorithmic mechanics, and time/space complexity.
   - **Bug Fixing:** Identifying root causes of errors (such as mutable default parameters) and producing verified fixes.
   - **Code Optimization:** Analyzing quadratic bottlenecks and refactoring algorithms to linear time.
4. An interactive **Streamlit Developer Assistant web application**.

---

## 📂 Project Structure

```
GenAI-Task(Assignment 38)-Parth_Dadhaniya/
├── config.py                 # Ollama connection configuration & local student CodeLlama emulator
├── part1_codellama_setup.py  # Task 1: Local Ollama installation guide & model health verification
├── part2_basic_interaction.py# Task 2: Basic CodeLlama prompts (prime check & basic explanation)
├── part3_code_assistant.py   # Tasks 3 & 5: 4 developer features & structured prompt engineering
├── app.py                    # Task 4: Interactive Streamlit developer assistant application
├── main.py                   # Master runner executing all tasks sequentially
├── assignment38.ipynb        # Interactive Jupyter Notebook
├── requirements.txt          # Python dependencies
└── README.md                 # Student assignment documentation
```

---

## 🚀 Tasks & Implementation Details

### Part 1 — Task 1: Setup CodeLlama with Ollama
- **File:** `part1_codellama_setup.py`
- **Installation Steps:**
  1. Install Ollama from `https://ollama.com`.
  2. Pull the model weights:
     ```bash
     ollama pull codellama:7b
     ```
  3. Start the background service:
     ```bash
     ollama serve
     ```
  4. The module automatically queries `http://localhost:11434/api/tags` to verify whether the daemon is online and whether `codellama:7b` is downloaded. If offline, the local student emulator activates seamlessly.

---

### Part 1 — Task 2: Basic CodeLlama Interaction
- **File:** `part2_basic_interaction.py`
- **LangChain Integration:** Connects via `OllamaLLM(model="codellama:7b", base_url="http://localhost:11434")`.
- **Tested Prompts:**
  1. *"Write a Python function to check prime numbers"* $\longrightarrow$ Returns $O(\sqrt{n})$ trial division with type hints and test assertions.
  2. *"Explain this code: def add(a, b): return a + b"* $\longrightarrow$ Breaks down operands, addition operator, and polymorphism.

---

### Part 1 & 2 — Tasks 3 & 5: Code Assistant Features & Prompt Engineering
- **File:** `part3_code_assistant.py`
- **Feature Breakdown & Prompt Templates:**

| Feature | Targeted Function | Prompt Engineering Guidelines |
| :--- | :--- | :--- |
| **1. Code Generation** | `generate_code(spec)` | Strict requirement for type annotations, descriptive docstrings, algorithmic complexity, and sample execution. |
| **2. Code Explanation** | `explain_code(code)` | Structured breakdown into: 1. High-Level Purpose, 2. Step-by-Step Logic, 3. Time & Auxiliary Space Complexity. |
| **3. Bug Fixing** | `debug_code(buggy_code, error)` | Diagnoses root causes (e.g., mutable default argument `lst=[]`), supplies corrected code with `lst=None`, and provides prevention takeaways. |
| **4. Code Optimization** | `optimize_code(code)` | Analyzes inefficiency bottlenecks (e.g. $O(n^2)$ nested loops) and refactors using hash sets to achieve $O(n)$ linear runtime. |

---

### Part 2 — Task 4: Streamlit Developer Assistant App
- **File:** `app.py`
- **Features:**
  - **Dynamic Task Selector:** Dropdown to switch between *Generate Code*, *Explain Code*, *Debug Code*, and *Optimize Code*.
  - **Adaptive Code Editor:** Expands and customizes placeholders and input height based on selected task.
  - **Error Diagnostics Field:** Optional input field to provide error messages or symptoms when debugging.
  - **Preset Quick-Load Buttons:** Sidebar buttons to test pre-configured code examples in one click.
  - **Formatted Code Output:** Displays syntax-highlighted code blocks with complexity analysis.

---

## 🛠️ How to Run

### 1. Installation
```bash
cd "GenAI-Task(Assignment 38)-Parth_Dadhaniya"
pip install -r requirements.txt
```

### 2. Optional: Run Live Local Ollama
To connect to real local weights:
```bash
ollama pull codellama:7b
ollama serve
```
*(If Ollama is not installed or offline, the project automatically runs using the verified student emulator.)*

### 3. Run the Master CLI Runner
```bash
python main.py
```

### 4. Run the Streamlit Developer Assistant App
```bash
streamlit run app.py
```

### 5. Launch the Jupyter Notebook
```bash
jupyter notebook assignment38.ipynb
```
