# task8_runnables_lcel.py
# Task 8: Runnables Basics & LCEL Composition
# Student: Parth Dadhaniya

import warnings
warnings.filterwarnings("ignore")

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
import config

print("=== Task 8: Runnables Basics & LCEL Composition ===")

llm = config.get_llm()

# 1. Custom python function wrapped with RunnableLambda
def count_words(text):
    words = text.strip().split()
    return {"text": text, "word_count": len(words)}

word_counter = RunnableLambda(count_words)

# 2. Pipe composition with RunnablePassthrough
prompt = PromptTemplate.from_template("Explain {topic} in simple terms.")
basic_chain = {"topic": RunnablePassthrough()} | prompt | llm | StrOutputParser()

print("\n--- 1. LCEL Pipe with RunnablePassthrough ---")
test_topic = "Machine Learning"
print(f"Input: {test_topic}")
print(f"Output:\n{basic_chain.invoke(test_topic).strip()}\n")

# 3. RunnablePassthrough.assign to add metadata
assign_chain = RunnablePassthrough.assign(
    word_info=lambda x: word_counter.invoke(x["topic"])
)

print("--- 2. RunnablePassthrough.assign ---")
assigned_data = assign_chain.invoke({"topic": "Deep Neural Networks"})
print(assigned_data)

# 4. Batch execution using standard Runnable method
print("\n--- 3. Runnable batch() Method ---")
batch_items = ["Natural Language Processing", "Computer Vision"]
batch_outputs = basic_chain.batch(batch_items)

for name, res in zip(batch_items, batch_outputs):
    print(f"\n[{name}]:")
    print(res.strip()[:100] + "...")

print("\n\nTask 8 completed successfully.")
