# Task 9: Final NLP Preprocessing Pipeline
# Author: Parth Dadhaniya

import re
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

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

def nlp_preprocess(text):
    if not isinstance(text, str):
        return ""
    
    # remove html tags, links, emails, and emojis
    text = re.sub(r"<.*?>", "", text)
    text = re.sub(r"&\w+;", "", text)
    text = re.sub(r"https?://\S+|www\.\S+", "", text)
    text = re.sub(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", "", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    
    # fix repeated letters and slang
    text = re.sub(r"(.)\1{2,}", r"\1", text)
    text = text.lower().strip()
    words = [slang_dict.get(w, w) for w in text.split()]
    text = " ".join(words)
    
    # remove punctuation and numbers
    text = re.sub(r"[^\w\s]", "", text)
    text = re.sub(r"\d+", "", text)
    
    # remove stopwords and lemmatize
    tokens = text.split()
    clean_tokens = [lemmatizer.lemmatize(w) for w in tokens if w not in stop_words and len(w) > 1]
    
    return " ".join(clean_tokens)

df = pd.read_csv("raw_text_data.csv")
df["final_clean_text"] = df["raw_text"].apply(nlp_preprocess)

print("Final NLP Pipeline Results (First 3 Samples):")
for i in range(3):
    print(f"\nOriginal: {df['raw_text'].iloc[i]}")
    print(f"Cleaned:  {df['final_clean_text'].iloc[i]}")

# save final dataset
df.to_csv("cleaned_text_final.csv", index=False)
print("\nSaved output to cleaned_text_final.csv")
