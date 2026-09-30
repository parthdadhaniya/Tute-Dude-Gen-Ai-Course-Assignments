---
title: GenAI Cloud Productivity Suite
emoji: 🚀
colorFrom: indigo
colorTo: purple
sdk: streamlit
sdk_version: "1.40.0"
app_file: app.py
pinned: false
license: mit
---

# Assignment 39: GenAI App Deployment (Streamlit Cloud & Hugging Face Spaces)

**Student:** Parth Dadhaniya  
**Course:** Generative AI Engineering — TuteDude  
**Topic:** Real-World Cloud Deployment of GenAI Applications, Streamlit Community Cloud, Hugging Face Spaces, YAML Metadata Configuration, CI/CD Workflows, and Platform Comparison  

---

## 📌 Problem Statement & Scenario

Deploying Generative AI applications to production requires transitioning from local development scripts to **globally accessible, containerized cloud web applications**. End-users need an intuitive interface to interact with GenAI pipelines without running local terminal commands or configuring local Python virtual environments.

In this assignment, we package and deploy a multi-tool **GenAI Cloud Productivity Suite** to two leading deployment platforms:
1. **Streamlit Community Cloud (`share.streamlit.io`):** Native GitHub-integrated continuous deployment.
2. **Hugging Face Spaces (`huggingface.co/spaces`):** High-performance cloud hosting integrated with the Hugging Face AI ecosystem.

---

## 📂 Project Structure

```
GenAI-Task(Assignment 39)-Parth_Dadhaniya/
├── .streamlit/
│   └── config.toml           # Headless server & dark theme styling configuration
├── config.py                 # Environment detection (Cloud vs Local) & pipeline logic
├── app.py                    # Multi-tool GenAI Suite (Summarizer, Code Assistant, Q&A)
├── part1_streamlit_cloud.py  # Task 1: Streamlit Cloud deployment guide & pre-flight check
├── part2_hf_spaces.py        # Task 2: Hugging Face Spaces guide & YAML metadata validation
├── part3_platform_comparison.py # Task 3: In-depth platform comparison & decision matrix
├── main.py                   # Master runner executing all deployment verification checks
├── assignment39.ipynb        # Interactive Jupyter Notebook
├── requirements.txt          # Production package dependencies
└── README.md                 # Documentation with Hugging Face Space YAML frontmatter
```

---

## 🚀 Tasks & Implementation Details

### Task 1: Deployment on Streamlit Cloud
- **File:** `part1_streamlit_cloud.py`
- **Workflow:**
  1. Commit `app.py`, `requirements.txt`, and `.streamlit/config.toml` to GitHub.
  2. Sign in to [Streamlit Community Cloud](https://share.streamlit.io) via GitHub OAuth.
  3. Select Repository: `parthdadhaniya/Tute-Dude-Gen-Ai-Course-Assignments`, Branch: `main`, and Main file path: `GenAI-Task(Assignment 39)-Parth_Dadhaniya/app.py`.
  4. Under Advanced Settings, configure secrets (e.g. `GROQ_API_KEY`).
  5. Deploy and access via the generated public URL: `https://<workspace>.streamlit.app`.
- **Pre-Flight Verification:** Automated validation checking entrypoint presence, dependency formatting, and pipeline responsiveness.

---

### Task 2: Deployment on Hugging Face Spaces
- **File:** `part2_hf_spaces.py`
- **Workflow:**
  1. Create a new Space at [Hugging Face Spaces](https://huggingface.co/spaces) with SDK set to **Streamlit**.
  2. Hardware selected: Free tier (2 vCPUs, 16GB RAM).
  3. Configure YAML metadata at the head of `README.md`:
     ```yaml
     ---
     title: GenAI Cloud Productivity Suite
     emoji: 🚀
     colorFrom: indigo
     colorTo: purple
     sdk: streamlit
     sdk_version: "1.40.0"
     app_file: app.py
     pinned: false
     license: mit
     ---
     ```
  4. Push repository files or configure a GitHub Actions sync workflow.
  5. The Space builds inside a container and serves at `https://huggingface.co/spaces/<username>/<space-name>`.

---

### Task 3: Validation & Platform Comparison
- **File:** `part3_platform_comparison.py`
- **Architectural Comparison:**

| Feature | Streamlit Community Cloud | Hugging Face Spaces |
| :--- | :--- | :--- |
| **Primary Focus** | Rapid dashboard prototyping | Full-scale ML & GenAI application hosting |
| **Free Tier Resources** | ~1 GB RAM (single container) | **16 GB RAM** (2 vCPUs, 50GB disk) |
| **GPU Acceleration** | Not available (CPU only) | On-demand paid upgrades (T4, A10G, A100) |
| **Supported SDKs** | Streamlit only | Streamlit, Gradio, Docker, Static HTML |
| **Deployment Trigger** | Direct GitHub commit hook | Hugging Face Git remote or GitHub Sync Action |
| **Secrets Management** | TOML editor (`st.secrets`) | Space Settings -> Variables & Secrets |
| **Community Reach** | Direct URL distribution | Native discovery on the Hugging Face Hub |

- **When to Use Which:**
  - **Use Streamlit Cloud** for lightweight enterprise dashboards, customer reporting, or lightweight GenAI wrappers calling external cloud LLM APIs (Groq, OpenAI) where memory consumption remains below 1GB.
  - **Use Hugging Face Spaces** when serving open-source deep learning pipelines (Transformers, PyTorch, Diffusers), requiring GPU acceleration, or engaging directly with the open-source ML research community.

---

## 🛠️ How to Run

### 1. Installation
```bash
cd "GenAI-Task(Assignment 39)-Parth_Dadhaniya"
pip install -r requirements.txt
```

### 2. Run the Verification Pipeline
```bash
python main.py
```

### 3. Run the Web Application Locally
```bash
streamlit run app.py
```

### 4. Launch the Interactive Notebook
```bash
jupyter notebook assignment39.ipynb
```
