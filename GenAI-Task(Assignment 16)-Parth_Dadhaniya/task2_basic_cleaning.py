# Task 2: Basic Text Cleaning
# Author: Parth Dadhaniya

import sys
import re
import pandas as pd

sys.stdout.reconfigure(encoding="utf-8")

df = pd.read_csv("customer_reviews.csv")

def basic_clean(text):
    # convert to lowercase
    text = text.lower()
    
    # remove punctuation
    text = re.sub(r"[^\w\s]", "", text)
    
    # remove numbers
    text = re.sub(r"\d+", "", text)
    
    # remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()
    
    return text

# store in clean_text_basic column
df["clean_text_basic"] = df["raw_text"].apply(basic_clean)

print("Basic Cleaning Results (First 3 Samples):")
for i in range(3):
    print(f"\nSample {i+1} Raw:")
    print(df["raw_text"].iloc[i])
    print(f"Sample {i+1} Cleaned (clean_text_basic):")
    print(df["clean_text_basic"].iloc[i])

# save to processed_text.csv
df.to_csv("processed_text.csv", index=False)
