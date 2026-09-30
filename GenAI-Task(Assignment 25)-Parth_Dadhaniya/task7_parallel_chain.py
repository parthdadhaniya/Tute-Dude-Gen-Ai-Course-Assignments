# task7_parallel_chain.py
# Task 7: Parallel Chain (RunnableParallel for Multi-Task Generation)
# Student: Parth Dadhaniya

import warnings
warnings.filterwarnings("ignore")

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
import config

print("=== Task 7: Parallel Chain ===")

llm = config.get_llm()

# branch 1: detailed answer
ans_chain = (
    PromptTemplate.from_template("Provide a concise explanation of: {topic}")
    | llm
    | StrOutputParser()
)

# branch 2: 1-sentence summary
summary_chain = (
    PromptTemplate.from_template("Summarize the main idea of {topic} in one short sentence:")
    | llm
    | StrOutputParser()
)

# branch 3: 2 follow-up questions
followup_chain = (
    PromptTemplate.from_template("Suggest 2 follow-up questions to study about {topic}:")
    | llm
    | StrOutputParser()
)

# combine all 3 into RunnableParallel
parallel_chain = RunnableParallel({
    "answer": ans_chain,
    "summary": summary_chain,
    "follow_up_questions": followup_chain
})

topics = [
    "Generative AI and Self-Attention Mechanisms",
    "Retrieval-Augmented Generation (RAG) Architecture"
]

print("\nExecuting Parallel Chain across 3 tasks:\n")
for i, topic in enumerate(topics, 1):
    print(f"=== Topic {i}: {topic} ===")
    output = parallel_chain.invoke({"topic": topic})
    
    print("\n[Branch 1: Answer]")
    print(output["answer"].strip())
    
    print("\n[Branch 2: Summary]")
    print(output["summary"].strip())
    
    print("\n[Branch 3: Follow-Up Questions]")
    print(output["follow_up_questions"].strip())
    print("\n" + "=" * 50)

print("Task 7 completed successfully.")
