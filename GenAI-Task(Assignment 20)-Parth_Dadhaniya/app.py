# Task 6: Simple Streamlit Web Application
# Author: Parth Dadhaniya

import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.title("Movie Recommendation System")
st.write("A simple content-based recommender built with TF-IDF and Cosine Similarity.")

# load dataset
df = pd.read_csv("cleaned_movies.csv")

# vectorize text and compute similarity
tfidf = TfidfVectorizer(max_features=5000, ngram_range=(1, 2))
tfidf_matrix = tfidf.fit_transform(df["clean_text"])
similarity = cosine_similarity(tfidf_matrix)

def recommend(movie_name, top_n=5):
    idx = df[df["title"].str.lower() == movie_name.lower()].index[0]
    distances = list(enumerate(similarity[idx]))
    sorted_movies = sorted(distances, key=lambda x: x[1], reverse=True)[1 : top_n + 1]

    results = []
    for i, score in sorted_movies:
        results.append((df.iloc[i]["title"], df.iloc[i]["genres"], round(score, 4)))
    return results

# dropdown to select movie
movie_list = df["title"].tolist()
selected_movie = st.selectbox("Select a movie from the catalog:", movie_list)

# button to generate recommendations
if st.button("Get Recommendations"):
    recommendations = recommend(selected_movie, top_n=5)
    st.subheader(f"Movies Recommended for '{selected_movie}':")
    for i, (title, genre, score) in enumerate(recommendations, 1):
        st.write(f"**{i}. {title}** ({genre}) — *similarity: {score}*")
