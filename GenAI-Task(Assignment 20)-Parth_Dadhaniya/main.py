# Assignment 20: Content-Based Movie Recommendation System
# Author: Parth Dadhaniya

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer, ENGLISH_STOP_WORDS
from sklearn.metrics.pairwise import cosine_similarity

print("Assignment 20: Content-Based Movie Recommendation System")
print("Author: Parth Dadhaniya\n")

# Task 1: Load Data
df = pd.read_csv("movies.csv")
print("Task 1: Dataset loaded successfully.")
print("Shape:   ", df.shape)
print("Columns: ", df.columns.tolist())

# Task 2: Preprocess Text
df["genres"] = df["genres"].fillna("")
df["overview"] = df["overview"].fillna("")
df["tags"] = df["genres"] + " " + df["overview"]

df["clean_text"] = df["tags"].str.lower().str.replace(r"[^\w\s]", " ", regex=True)
stop_words = set(ENGLISH_STOP_WORDS)
df["clean_text"] = df["clean_text"].apply(
    lambda x: " ".join([w for w in x.split() if w not in stop_words])
)
df.to_csv("cleaned_movies.csv", index=False)
print("\nTask 2: Text cleaning complete. Saved to cleaned_movies.csv")

# Task 3: TF-IDF Vectorization
tfidf = TfidfVectorizer(max_features=5000, ngram_range=(1, 2))
tfidf_matrix = tfidf.fit_transform(df["clean_text"])
print(f"\nTask 3: TF-IDF Matrix Shape: {tfidf_matrix.shape}")

# Task 4: Cosine Similarity
similarity = cosine_similarity(tfidf_matrix)
print(f"\nTask 4: Cosine Similarity Matrix Shape: {similarity.shape}")

# Task 5: Recommendation Function
def recommend(movie_name, top_n=5):
    idx = df[df["title"].str.lower() == movie_name.lower()].index[0]
    distances = list(enumerate(similarity[idx]))
    sorted_movies = sorted(distances, key=lambda x: x[1], reverse=True)[1 : top_n + 1]
    return [(df.iloc[i]["title"], df.iloc[i]["genres"], round(score, 4)) for i, score in sorted_movies]

print("\nTask 5: Recommendations for 3 sample movies:")
for test_movie in ["The Dark Knight", "Inception", "Toy Story"]:
    print(f"\nRecommendations for '{test_movie}':")
    for title, genre, score in recommend(test_movie):
        print(f"  - {title} ({genre}) | similarity: {score}")

print("\nAll pipeline tasks executed successfully!")
print("Run 'streamlit run app.py' to open the web interface.")
