# Task 3: Advanced Noise Removal
# Author: Parth Dadhaniya

import sys
import re
import pandas as pd

sys.stdout.reconfigure(encoding="utf-8")

df = pd.read_csv("customer_reviews.csv")

def advanced_noise_removal(text):
    # remove HTML tags like <div>, <p>, <b>
    text = re.sub(r"<.*?>", "", text)
    text = re.sub(r"&\w+;", "", text)
    
    # remove URLs
    text = re.sub(r"https?://\S+|www\.\S+", "", text)
    
    # remove email addresses
    text = re.sub(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", "", text)
    
    # remove emojis and non-ascii characters
    text = text.encode("ascii", "ignore").decode("ascii")
    
    # remove punctuation and numbers
    text = re.sub(r"[^\w\s]", "", text)
    text = re.sub(r"\d+", "", text)
    
    # lowercase and remove extra whitespace
    text = text.lower()
    text = re.sub(r"\s+", " ", text).strip()
    
    return text

# store in clean_text_advanced column
df["clean_text_advanced"] = df["raw_text"].apply(advanced_noise_removal)

print("Advanced Cleaning Results (First 3 Samples):")
for i in range(3):
    print(f"\nSample {i+1} Raw:")
    print(df["raw_text"].iloc[i])
    print(f"Sample {i+1} Cleaned (clean_text_advanced):")
    print(df["clean_text_advanced"].iloc[i])

# save to processed_text.csv
df.to_csv("processed_text.csv", index=False)
