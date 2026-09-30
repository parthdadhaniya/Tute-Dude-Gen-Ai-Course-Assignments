# task3_pydantic_schema.py
# Task 3: Pydantic Output Schema
# Student: Parth Dadhaniya

import warnings
warnings.filterwarnings("ignore")

from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
import config

print("=== Task 3: Pydantic Output Schema ===")

# define pydantic model
class Answer(BaseModel):
    answer: str = Field(description="Direct answer to the question")
    confidence: float = Field(description="Confidence score between 0.0 and 1.0")
    source: str = Field(description="Source document name or citation")

parser = PydanticOutputParser(pydantic_object=Answer)

prompt = PromptTemplate(
    template="""Answer the user question accurately.
Provide a confidence score and source document citation.

{format_instructions}

Question: {question}
""",
    input_variables=["question"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

llm = config.get_llm()
chain = prompt | llm | parser

test_queries = [
    "What is machine learning and how does it learn from data?",
    "What columns and information does our employee CSV dataset contain?"
]

print("\nTesting Pydantic Output Parser:\n")
for i, q in enumerate(test_queries, 1):
    print(f"--- Query {i} ---")
    print(f"Question: {q}")
    
    result = chain.invoke({"question": q})
    print("\nParsed Result:")
    print(f"Answer     : {result.answer}")
    print(f"Confidence : {result.confidence}")
    print(f"Source     : {result.source}")
    print(f"JSON Dump  :\n{result.model_dump_json(indent=2)}\n")

print("Task 3 completed successfully.")
