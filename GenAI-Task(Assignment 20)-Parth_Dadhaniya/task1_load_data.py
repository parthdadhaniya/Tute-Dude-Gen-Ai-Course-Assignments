# Task 1: Load & Understand Dataset
# Author: Parth Dadhaniya

import pandas as pd

# dataset: TMDB 5000 Movie Dataset (Kaggle)
# link: https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

df = pd.read_csv("movies.csv")

print("Dataset Shape:", df.shape)
print("\nColumns in Dataset:")
print(df.columns.tolist())

print("\nFirst 5 Rows:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nText columns selected for recommendation:")
print("- 'genres' and 'overview' (combined to capture movie content)")
print("- 'title' (used as the movie identifier)")
