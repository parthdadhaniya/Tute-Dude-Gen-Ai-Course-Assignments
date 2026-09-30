# Assignment 27: Chatbots with Conversation History using LangChain

**Student:** Parth Dadhaniya  
**Course:** GenAI - TuteDude  

---

## Overview

In real-world applications, chatbots need to remember past interactions to understand context and follow-up questions. At the same time, we must prevent conversations from growing too long, which causes token overflow and high API costs.

In this assignment, I implemented:
- Chat messages (`SystemMessage`, `HumanMessage`, `AIMessage`)
- `MessagesPlaceholder` to pass dynamic conversation history into prompt templates
- Basic message history storage in lists
- Chat history trimming (sliding window)
- A multi-turn Q&A chatbot that remembers context
- A stateful chatbot application supporting multiple sessions
- An optional Streamlit web chat UI

---

## File Structure

```text
GenAI-Task(Assignment 27)-Parth_Dadhaniya/
├── config.py                           # Model configuration (Groq or local fallback)
├── task1_task2_messages_placeholder.py # Part 1: Chat messages & MessagesPlaceholder
├── task3_task4_history_trimming.py     # Part 2: Message history & trimming
├── task5_qa_chatbot.py                 # Part 3: Q&A Chatbot with follow-up testing
├── task6_stateful_app.py               # Part 3: Stateful chatbot mini project & CLI
├── streamlit_app.py                    # Part 3: Optional Streamlit web interface
├── task7_observations.py               # Part 3: Conceptual observations & insights
├── main.py                             # Master runner for all tasks
├── assignment27.ipynb                  # Jupyter notebook
├── requirements.txt                    # Project requirements
└── README.md                           # Documentation
```

---

## Tasks Summary

### Part 1: Messages & Message Placeholders
- **Task 1:** Explained the three core message types in LangChain:
  - `SystemMessage`: Defines the personality, rules, and behavior of the chatbot.
  - `HumanMessage`: Represents the message sent by the user.
  - `AIMessage`: Represents the response from the LLM.
  - Message-based prompting is superior to raw string prompts because it cleanly separates instructions from user text and makes adding history turns trivial.
- **Task 2:** Built a `ChatPromptTemplate` using `MessagesPlaceholder(variable_name="chat_history")`. Successfully tested dynamic injection over 3 turns.

### Part 2: History Management & Trimming
- **Task 3:** Implemented a basic history list. Showed that after 4 turns, history grows to 8 messages.
- **Task 4:** Implemented a sliding window trimming function (`trim_history`). Confirmed that keeping the last 4 messages prevents token overflow while preserving recent context.

### Part 3: Q&A Chatbot & Stateful Application
- **Task 5:** Built `QAChatbot` and tested follow-up queries:
  1. *"Explain Python lists"* -> Explains mutable lists.
  2. *"Give an example"* -> Correctly returns a list example without repeating "list".
  3. *"What about tuples?"* -> Explains immutable tuples and contrasts with lists.
  4. *"Can we modify a tuple like we modified a list?"* -> Answers based on the previous turns.
- **Task 6:** Built `StatefulChatbot` supporting multiple isolated user sessions (`user_1`, `user_2`), automated sliding window trimming, and session reset.
- **Task 7:** Documented insights on token costs, latency trade-offs, trimming vs summarizing, and `MessagesPlaceholder` vs memory objects.

---

## How to Run

### Run All Tasks (Master Script)
```bash
python main.py
```

### Run Individual Scripts
```bash
python task1_task2_messages_placeholder.py
python task3_task4_history_trimming.py
python task5_qa_chatbot.py
python task6_stateful_app.py
python task7_observations.py
```

### Interactive Terminal Chat
```bash
python task6_stateful_app.py --interactive
```

### Run Optional Streamlit UI
```bash
streamlit run streamlit_app.py
```
