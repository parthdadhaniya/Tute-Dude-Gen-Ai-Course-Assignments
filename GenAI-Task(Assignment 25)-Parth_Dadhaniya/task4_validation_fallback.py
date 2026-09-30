# task4_validation_fallback.py
# Task 4: Validation & Error Handling with Fallback
# Student: Parth Dadhaniya

import json
import warnings
warnings.filterwarnings("ignore")

from pydantic import BaseModel, Field
from langchain_core.exceptions import OutputParserException
from langchain_core.output_parsers import PydanticOutputParser

print("=== Task 4: Validation & Error Handling ===")

class Answer(BaseModel):
    answer: str = Field(description="Direct answer")
    confidence: float = Field(description="Confidence between 0.0 and 1.0")
    source: str = Field(description="Source citation")

parser = PydanticOutputParser(pydantic_object=Answer)

def parse_with_fallback(raw_text, default_source="fallback_recovery"):
    """
    Parses LLM text into Answer model.
    Falls back gracefully if the text is invalid JSON or misses fields.
    """
    try:
        return parser.parse(raw_text)
    except OutputParserException as err:
        print(f"  [Validation Error] Output does not match schema: {err.__class__.__name__}")
        print("  [Fallback] Extracting available text into default Answer object.")
        clean_text = raw_text.replace("```json", "").replace("```", "").strip()
        return Answer(
            answer=clean_text if clean_text else "No answer provided.",
            confidence=0.50,
            source=default_source
        )

# scenario 1: Valid JSON
print("\n--- 1. Testing Valid JSON ---")
valid_input = """{
  "answer": "LangChain pipelines connect prompts, models, and parsers into LCEL chains.",
  "confidence": 0.95,
  "source": "data/notes.txt"
}"""
res1 = parse_with_fallback(valid_input)
print("Result:", res1.model_dump())

# scenario 2: Malformed plain text
print("\n--- 2. Testing Malformed Output (Plain Text) ---")
malformed_input = "Here is an answer, but I did not format it as JSON."
res2 = parse_with_fallback(malformed_input)
print("Result:", res2.model_dump())

# scenario 3: Incomplete JSON missing fields
print("\n--- 3. Testing Incomplete JSON ---")
incomplete_input = """{
  "answer": "Only the answer field is present."
}"""
res3 = parse_with_fallback(incomplete_input)
print("Result:", res3.model_dump())

print("\nTask 4 completed successfully.")
