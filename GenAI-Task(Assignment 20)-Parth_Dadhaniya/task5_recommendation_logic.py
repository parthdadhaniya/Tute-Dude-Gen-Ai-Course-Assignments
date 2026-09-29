# Task 5: Recommendation Logic Function
# Author: Parth Dadhaniya

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("cleaned_movies.csv")

# compute similarity
tfidf = TfidfVectorizer(max_features=5000, ngram_range=(1, 2))
tfidf_matrix = tfidf.fit_transform(df["clean_text"])
similarity = cosine_similarity(tfidf_matrix)

def recommend(item_name, top_n=5):
    # 1. find index of selected movie
    try:
        idx = df[df["title"].str.lower() == item_name.lower()].index[0]
    except IndexError:
        print(f"Movie '{item_name}' not found!")
        return []

    # 2. get similarity scores for all movies
    distances = list(enumerate(similarity[idx]))

    # 3. sort movies based on similarity score (skip index 0 which is itself)
    sorted_movies = sorted(distances, key=lambda x: x[1], reverse=True)[1 : top_n + 1]

    # return recommended titles
    print(f"\nTop {top_n} Recommendations for '{item_name}':")
    recs = []
    for i, score in sorted_movies:
        title = df.iloc[i]["title"]
        genres = df.iloc[i]["genres"]
        recs.append(title)
        print(f"- {title} ({genres}) | score: {score:.4f}")
    return recs

# test with 3 different movies
recommend("The Dark Knight")
recommend("Inception")
recommend("Toy Story")
