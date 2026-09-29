# Task 1: Manual One-Hot Encoding (Text Level)
# Author: Parth Dadhaniya

import pandas as pd

# load cleaned dataset
df = pd.read_csv("cleaned_text_dataset.csv")

# pick 5 short sentences
sentences = df["final_clean_text"].head(5).tolist()

print("Selected 5 Sentences:")
for i, s in enumerate(sentences, 1):
    print(f"Sentence {i}: {s}")

# find unique words across the 5 sentences
vocab = sorted(list(set(" ".join(sentences).split())))
print("\nVocabulary Size:", len(vocab))
print("Vocabulary:", vocab[:10], "...")

# build one-hot vectors manually
one_hot_matrix = []
for s in sentences:
    words = set(s.split())
    # 1 if word is present in sentence, else 0
    row = [1 if w in words else 0 for w in vocab]
    one_hot_matrix.append(row)

# display vectors
print("\nOne-Hot Vectors for Each Sentence:")
for i, row in enumerate(one_hot_matrix, 1):
    print(f"Sentence {i} (Length {len(row)}): {row[:10]} ...")

# show in a dataframe
df_ohe = pd.DataFrame(one_hot_matrix, columns=vocab, index=[f"Sentence {i+1}" for i in range(5)])
print("\nOne-Hot Encoded Table (First 6 Columns):")
print(df_ohe.iloc[:, :6])
