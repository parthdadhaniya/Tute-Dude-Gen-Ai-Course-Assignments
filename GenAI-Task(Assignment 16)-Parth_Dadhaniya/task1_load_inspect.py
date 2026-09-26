# Task 1: Load Text Dataset and Identify Common Raw Text Issues
# Author: Parth Dadhaniya

import sys
import pandas as pd

sys.stdout.reconfigure(encoding="utf-8")

# load the dataset
df = pd.read_csv("customer_reviews.csv")

print("Dataset loaded successfully.")
print("Total rows:", len(df))
print("Columns:", list(df.columns))

# print first 5 text samples with length
print("\nFirst 5 Samples and Their Lengths:")
for i, row in df.head(5).iterrows():
    text = row["raw_text"]
    print(f"\nSample {row['id']} [{row['category']}] (Length: {len(text)} characters):")
    print(text)

# common issues in raw text
print("\nCommon Raw Text Issues Found:")
print("1. HTML tags: <p>, <div>, <b>, <span>, and &amp;")
print("2. URLs: links like https://shop.com/phone2024 and https://techreviews.org/laptop")
print("3. Email addresses: support@gadgets.com, refund@store.org")
print("4. Emojis and special symbols: 🔥, 👍, 😡, ⭐, 👎")
print("5. Numbers and dates: 24, 14, 2024, #90210, $29.99")
print("6. Inconsistent casing: ALL CAPS words like EVER, NEVER BUYING AGAIN")
print("7. Punctuation: multiple exclamation marks (!!!) and dots (...)")
print("8. Stopwords: common words like the, is, at, was, and, for")
