# Task 2: Basic Text Cleaning
# Author: Parth Dadhaniya

import re
import pandas as pd

df = pd.read_csv("raw_text_data.csv")

def basic_clean(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)       # remove punctuation
    text = re.sub(r"\d+", "", text)           # remove numbers
    text = re.sub(r"\s+", " ", text).strip()  # remove extra spaces
    return text

# save to clean_text_basic column
df["clean_text_basic"] = df["raw_text"].apply(basic_clean)

# compare original vs cleaned text
print("Original vs Cleaned (First 3 Samples):")
for i in range(3):
    print(f"\nSample {i+1} Original:")
    print(" ", df["raw_text"].iloc[i])
    print(f"Sample {i+1} Cleaned:")
    print(" ", df["clean_text_basic"].iloc[i])

# save intermediate file
df.to_csv("processed_text.csv", index=False)
print("\nSaved output to processed_text.csv")
