# Assignment 36: HuggingFace Integration with LangChain

**Student:** Parth Dadhaniya  
**Course:** Generative AI Engineering — TuteDude  
**Topic:** Hugging Face Open-Source Models, LangChain Integration, Replacing Closed APIs, and Prompt Engineering  

---

## 📌 Problem Statement & Scenario

Many enterprise GenAI architectures require moving away from closed, proprietary APIs (like OpenAI) to **open-source Hugging Face models** to achieve:
1. **Data Sovereignty & Privacy:** Sensitive company data never leaves private infrastructure.
2. **Cost Predictability:** Eliminate per-token billing and sudden API pricing adjustments.
3. **Model Autonomy & Customization:** Direct control over model weights, fine-tuning, and deployment pipelines.

In this assignment, we integrate Hugging Face models with **LangChain**, replace OpenAI in production-style chains, and evaluate system-prompt steering using `ChatPromptTemplate`.

---

## 📂 Project Structure

```
GenAI-Task(Assignment 36)-Parth_Dadhaniya/
├── config.py                 # Hugging Face token config & LangChain LLM factory with offline student fallback
├── part1_hf_direct.py        # Task 1: Direct Hugging Face model inference & output quality observation
├── part2_hf_langchain.py     # Task 2: LangChain wrapper integration & replacing OpenAI across 3 prompts
├── part3_chat_prompt.py      # Task 3: ChatPromptTemplate (System + Human) vs Normal Prompt comparison
├── main.py                   # Master runner executing Tasks 1, 2, and 3
├── assignment36.ipynb        # Interactive Jupyter Notebook with cell outputs
├── requirements.txt          # Python dependencies
└── README.md                 # Student assignment documentation
```

---

## 🚀 Tasks & Implementation Details

### Part 1: Getting Started with Hugging Face Models
- **File:** `part1_hf_direct.py`
- **Objective:** Directly query open-source Hugging Face models (e.g., `google/flan-t5-base`, `mistralai/Mistral-7B-Instruct-v0.2`) via `InferenceClient` or the serverless inference router.
- **Tested Prompts:**
  1. *Knowledge Retrieval:* "What is Generative AI? Explain in two sentences."
  2. *Sequence-to-Sequence Translation:* "Translate English to French: The weather is beautiful today."
- **Output Quality Observations:**
  - **Instruction Adherence:** Flan-T5 is an instruction-tuned Seq2Seq model that adheres strictly to length constraints without unnecessary chit-chat.
  - **Coherence & Accuracy:** Grammatical correctness and clean semantic translation.
  - **Latency:** Sub-second latency for lightweight (~250M parameter) models.

---

### Part 2: Hugging Face with LangChain (Replacing OpenAI)
- **File:** `part2_hf_langchain.py`
- **Objective:** Swap closed OpenAI APIs with Hugging Face using LangChain's unified `Runnable` ecosystem.
- **Code Transition:**
  ```python
  # Previous (OpenAI closed API):
  from langchain_openai import ChatOpenAI
  llm = ChatOpenAI(model="gpt-3.5-turbo")

  # New (Hugging Face Open-Source):
  from langchain_huggingface import HuggingFaceEndpoint
  llm = HuggingFaceEndpoint(repo_id="google/flan-t5-base", max_new_tokens=256)

  # Unified LCEL Chain:
  chain = prompt_template | llm | StrOutputParser()
  ```
- **Tested Prompt Categories:**
  1. **Factual / Technical Q&A:** Differences between supervised and unsupervised learning.
  2. **Code Generation:** Writing a Python string reversal function with slice notation `[::-1]`.
  3. **Enterprise Strategy:** 3 core advantages of open-source models over closed APIs.

---

### Part 3: Chat Prompt Template with Hugging Face
- **File:** `part3_chat_prompt.py`
- **Objective:** Compare structured `ChatPromptTemplate` (System + Human messages) against flat `PromptTemplate`.
- **Target Question:** *"What is temperature in Large Language Models?"*
- **Comparison Table:**

| Feature | Normal `PromptTemplate` | `ChatPromptTemplate` |
| :--- | :--- | :--- |
| **Message Structure** | Single unstructured raw text | Distinct System and Human messages |
| **Persona Enforcement** | Weak / Unspecified | Strict (Adopts AI educator persona with kitchen/stove analogy) |
| **Tone & Style** | Academic, direct definition | Encouraging, metaphorical, user-friendly |
| **Prompt Injection Defense** | Lower (everything in one stream) | Higher (token delimiter tags isolate instructions) |
| **Model Chat Support** | Raw completion format | Automatically formatted to chat templates (`[INST]...[/INST]`) |

---

## 🛠️ How to Run

### 1. Prerequisites & Installation
```bash
cd "GenAI-Task(Assignment 36)-Parth_Dadhaniya"
pip install -r requirements.txt
```

### 2. Optional: Configure Hugging Face API Token
To connect to live Hugging Face Inference endpoints, create a `.env` file in the project folder:
```env
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token_here
```
*(If no token is supplied, the project automatically uses the offline student model runner so all chains and evaluations run cleanly without errors.)*

### 3. Run the Master CLI Runner
```bash
python main.py
```

### 4. Run Individual Modules
```bash
python part1_hf_direct.py     # Run Task 1
python part2_hf_langchain.py  # Run Task 2
python part3_chat_prompt.py   # Run Task 3
```

### 5. Run the Jupyter Notebook
```bash
jupyter notebook assignment36.ipynb
```
