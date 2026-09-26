# Task 9: Complete NLP Preprocessing Pipeline
# Author: Parth Dadhaniya

import sys
import re
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

sys.stdout.reconfigure(encoding="utf-8")

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

# end-to-end preprocessing pipeline function
def nlp_preprocess(text):
    if not isinstance(text, str):
        return ""
    
    # 1. remove HTML tags & entities
    text = re.sub(r"<.*?>", "", text)
    text = re.sub(r"&\w+;", "", text)
    
    # 2. remove URLs
    text = re.sub(r"https?://\S+|www\.\S+", "", text)
    
    # 3. remove email addresses
    text = re.sub(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", "", text)
    
    # 4. remove emojis and non-ascii
    text = text.encode("ascii", "ignore").decode("ascii")
    
    # 5. remove punctuation and numbers
    text = re.sub(r"[^\w\s]", "", text)
    text = re.sub(r"\d+", "", text)
    
    # 6. lowercase and normalize whitespace
    text = text.lower().strip()
    
    # 7. split into tokens
    tokens = text.split()
    
    # 8. remove stopwords and lemmatize
    clean_tokens = [
        lemmatizer.lemmatize(word)
        for word in tokens
        if word not in stop_words and len(word) > 1
    ]
    
    # 9. join back into clean string
    return " ".join(clean_tokens)

# load dataset
df = pd.read_csv("customer_reviews.csv")

# apply pipeline and store in final_clean_text
df["final_clean_text"] = df["raw_text"].apply(nlp_preprocess)

print("Final NLP Pipeline Results (First 5 Samples):")
for i in range(5):
    print(f"\nSample {i+1} Raw:")
    print(" ", df["raw_text"].iloc[i])
    print(f"Sample {i+1} Final Clean:")
    print(" ", df["final_clean_text"].iloc[i])

# save to cleaned_reviews_final.csv
df.to_csv("cleaned_reviews_final.csv", index=False)
print("\nSaved final cleaned data to cleaned_reviews_final.csv")
