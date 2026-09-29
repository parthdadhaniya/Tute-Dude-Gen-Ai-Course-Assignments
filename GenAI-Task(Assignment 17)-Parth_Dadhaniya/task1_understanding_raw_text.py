# Task 1: Understanding Raw Text Data
# Author: Parth Dadhaniya

import pandas as pd

# read the dataset
df = pd.read_csv("raw_text_data.csv")

print("Dataset loaded successfully.")
print("Total rows:", len(df))
print("Columns:", list(df.columns))

# print first 5 text samples with length
print("\nFirst 5 Samples and Their Lengths:")
for i, row in df.head(5).iterrows():
    text = row["raw_text"]
    print(f"\nSample {row['id']} [{row['category']}] (Length: {len(text)} chars):")
    print(text)

# common raw text issues
print("\nCommon Issues Found in Raw Text:")
print("- Uppercase / lowercase mismatch: ALL-CAPS words like 'BEST MOVIE' and 'ASAP'")
print("- Punctuation: repeated marks like '!!!', '???', '...'")
print("- Numbers: dates, prices, ratings like 2024, $49.99, 5/5")
print("- Extra spaces: irregular spacing around punctuation and tags")
print("- Web noise: URLs like https://moviehub.com and emails like info@cinema.com")
print("- HTML tags: <div>, <b>, <p>, <span>")
print("- Emojis: 🔥, 🎬, 😡, 👎, ⭐")
print("- Slang and repeated letters: 'soooo', 'u', 'gr8', 'pls'")
