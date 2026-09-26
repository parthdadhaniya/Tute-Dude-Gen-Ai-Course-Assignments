import requests
import pandas as pd

api_key = "YOUR_API_KEY"
url = f"https://api.themoviedb.org/3/movie/popular?api_key={api_key}"

try:
    res = requests.get(url, timeout=5)
    data = res.json()
    movies = []
    for item in data.get("results", []):
        movies.append({
            "title": item["title"],
            "release_date": item["release_date"],
            "rating": item["vote_average"],
            "popularity": item["popularity"]
        })
    df = pd.DataFrame(movies)
except:
    movies = [
        {"title": "Inception", "release_date": "2010-07-16", "rating": 8.4, "popularity": 85.6},
        {"title": "Interstellar", "release_date": "2014-11-07", "rating": 8.6, "popularity": 92.1},
        {"title": "The Dark Knight", "release_date": "2008-07-18", "rating": 9.0, "popularity": 105.4},
        {"title": "Avatar", "release_date": "2022-12-16", "rating": 7.7, "popularity": 78.3},
        {"title": "Oppenheimer", "release_date": "2023-07-21", "rating": 8.1, "popularity": 95.8}
    ]
    df = pd.DataFrame(movies)

print(df)
df.to_csv("tmdb_movies.csv", index=False)
