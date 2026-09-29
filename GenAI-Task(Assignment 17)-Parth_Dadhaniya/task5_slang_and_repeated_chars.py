# Task 5: Handling Repeated Characters & Slang
# Author: Parth Dadhaniya

import re
import pandas as pd

df = pd.read_csv("raw_text_data.csv")

# slang words mapping
slang_dict = {
    "u": "you",
    "gr8": "great",
    "pls": "please",
    "thx": "thanks",
    "omg": "oh my god",
    "bcoz": "because",
    "idk": "i do not know",
    "asap": "as soon as possible",
    "mins": "minutes"
}

def clean_slang_and_repeats(text):
    # reduce repeated letters like 'soooo' to 'so'
    text = re.sub(r"(.)\1{2,}", r"\1", text)
    
    # replace slang words
    words = text.split()
    words = [slang_dict.get(w.lower(), w) for w in words]
    return " ".join(words)

# test on sample sentence
example = "omg this phone battery is terribleeee... pls fix it u guys promised gr8 performance"
print("Example Before:", example)
print("Example After: ", clean_slang_and_repeats(example))

# apply to dataset
df["clean_text_slang"] = df["raw_text"].apply(clean_slang_and_repeats)

print("\nSample from Dataset:")
print("Original:", df["raw_text"].iloc[1])
print("Cleaned: ", df["clean_text_slang"].iloc[1])

df.to_csv("processed_text.csv", index=False)
print("\nSaved output to processed_text.csv")
