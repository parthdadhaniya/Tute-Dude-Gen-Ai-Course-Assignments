# Task 3: Removing Noise (Advanced Cleaning)
# Author: Parth Dadhaniya

import re
import pandas as pd

df = pd.read_csv("raw_text_data.csv")

def advanced_noise_removal(text):
    text = re.sub(r"<.*?>", "", text)                                           # remove html tags
    text = re.sub(r"&\w+;", "", text)                                           # remove html entities
    text = re.sub(r"https?://\S+|www\.\S+", "", text)                           # remove urls
    text = re.sub(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", "", text)  # remove emails
    text = text.encode("ascii", "ignore").decode("ascii")                       # remove emojis and non-ascii
    text = re.sub(r"[^\w\s]", "", text)                                         # remove punctuation
    text = re.sub(r"\d+", "", text)                                             # remove digits
    text = text.lower()
    text = re.sub(r"\s+", " ", text).strip()                                    # remove extra spaces
    return text

# save to clean_text_advanced column
df["clean_text_advanced"] = df["raw_text"].apply(advanced_noise_removal)

print("Advanced Noise Removal (First 3 Samples):")
for i in range(3):
    print(f"\nSample {i+1} Raw:")
    print(" ", df["raw_text"].iloc[i])
    print(f"Sample {i+1} Cleaned:")
    print(" ", df["clean_text_advanced"].iloc[i])

df.to_csv("processed_text.csv", index=False)
print("\nSaved output to processed_text.csv")
