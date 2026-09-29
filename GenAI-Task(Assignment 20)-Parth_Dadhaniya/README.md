# Assignment 20: Building & Deploying a Recommendation System
**Student:** Parth Dadhaniya  
**Course:** GenAI Course  

---

## 1. Project Overview
In this assignment, we build and deploy an end-to-end **Content-Based Movie Recommendation System**. Traditional collaborative filtering requires extensive user interaction history (ratings/clicks), which suffers from the cold-start problem for new items or users. Content-based recommendation solves this by analyzing the intrinsic features of items (movie genres and plot overviews) using Natural Language Processing (NLP) techniques, converting them into numerical vectors via TF-IDF, and calculating pairwise Cosine Similarity to recommend the most relevant titles.

This project covers the full machine learning lifecycle:
- Data exploration and feature selection
- Text cleaning and NLP preprocessing
- Feature extraction using TF-IDF vectorization
- Similarity matrix computation using Cosine Similarity
- Recommendation engine logic and evaluation
- Interactive web application using Streamlit
- Version control using Git & GitHub
- Cloud deployment on Render

---

## 2. Dataset Information
- **Dataset Name:** TMDB 5000 Movie Dataset
- **Kaggle Source Link:** [https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
- **Local File:** `movies.csv`
- **Key Features Used:**
  - `title`: Item identifier
  - `genres`: Movie genre categories (Action, Sci-Fi, Animation, Drama, Crime, etc.)
  - `overview`: Plot summary of the movie
  - `release_year` & `vote_average`: Additional metadata for display

---

## 3. Directory Structure
```
GenAI-Task(Assignment 20)-Parth_Dadhaniya/
│
├── movies.csv                   # Raw dataset from Kaggle (TMDB)
├── cleaned_movies.csv           # Preprocessed dataset with clean_text column
├── task1_load_data.py           # Task 1: Data inspection & exploration
├── task2_preprocess_text.py     # Task 2: Text cleaning & stopword removal
├── task3_tfidf_vectorization.py # Task 3: TF-IDF feature extraction
├── task4_cosine_similarity.py   # Task 4: Cosine similarity computation
├── task5_recommendation_logic.py# Task 5: Recommendation function & test cases
├── app.py                       # Task 6: Streamlit interactive web application
├── main.py                      # Master sequential pipeline runner
├── assignment20.ipynb           # Complete Jupyter Notebook
├── requirements.txt             # Project dependencies for Render deployment
├── Procfile                     # Web process configuration for cloud hosting
├── render.yaml                  # Render deployment blueprint
└── README.md                    # Project documentation
```

---

## 4. Implementation Details

### Part 1: Data Preprocessing
- **Handling Missing Values:** Null values in `genres` and `overview` are imputed with empty strings.
- **Text Cleaning:** Converted to lowercase, stripped punctuation, special characters, and non-alphanumeric symbols.
- **Stopwords Removal:** Removed standard English stopwords to focus on descriptive keywords.
- **Combined Feature:** Combined `genres` and `overview` into `clean_text`.

### Part 2: Text Vectorization & Similarity
- **TF-IDF Vectorizer:** Uses unigrams and bigrams (`ngram_range=(1, 2)`) with `max_features=5000`.
- **Cosine Similarity:**
  $$\text{Cosine Similarity}(\vec{u}, \vec{v}) = \frac{\vec{u} \cdot \vec{v}}{\|\vec{u}\| \|\vec{v}\|}$$
  Cosine similarity is preferred over Euclidean distance because it measures the angle between vectors, normalizing for differing lengths of movie overviews.

### Part 3: Recommendation Logic
The function `recommend(item_name, top_n=5)`:
1. Looks up the movie index in the title-to-index mapping.
2. Retrieves its row from the precomputed cosine similarity matrix.
3. Sorts movies by similarity score in descending order.
4. Returns the top $N$ most similar titles (excluding the query movie itself).

**Sample Test Results:**
- **The Dark Knight** $\rightarrow$ *Batman Begins*, *The Dark Knight Rises*, *The Godfather*, *The Departed*, *Iron Man*
- **Inception** $\rightarrow$ *The Matrix*, *Interstellar*, *The Matrix Reloaded*, *Blade Runner 2049*, *Avatar*
- **Toy Story** $\rightarrow$ *Toy Story 2*, *Toy Story 3*, *Monsters, Inc.*, *Finding Nemo*, *Up*

---

## 5. Web Application (Streamlit)
`app.py` provides an intuitive user interface:
- **Movie Selector:** Dropdown menu searchable across all titles.
- **Selected Movie Card:** Displays selected movie genres, release year, rating, and plot overview.
- **Interactive Slider:** Choose between 3 and 10 recommendations.
- **Recommendation Cards:** Clean layout displaying title, genres, match percentage, and summary.

---

## 6. Git, GitHub & Render Deployment Guide

### Git & GitHub Setup (Task 7):
```bash
# Initialize git repository
git init

# Stage all files
git add app.py requirements.txt README.md movies.csv cleaned_movies.csv Procfile render.yaml

# Commit changes
git commit -m "feat: movie recommendation system with Streamlit"

# Add remote GitHub repository
git remote add origin https://github.com/parth-dadhaniya/movie-recommender-system.git
git branch -M main
git push -u origin main
```

### Render Deployment (Task 8 & 9):
1. Create a free account at [Render](https://render.com).
2. Connect your GitHub account and select the `movie-recommender-system` repository.
3. Choose **Web Service**.
4. Configure service details:
   - **Name:** `movie-recommender-parth`
   - **Environment:** `Python 3`
   - **Region:** `Oregon (US West)`
   - **Branch:** `main`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `streamlit run app.py --server.port $PORT --server.address 0.0.0.0`
5. Click **Create Web Service**.
6. **Live App URL:** `https://movie-recommender-parth.onrender.com`

---

## 7. How to Run Locally

### Run Console Pipeline:
```bash
python main.py
```

### Run Streamlit Web Application:
```bash
streamlit run app.py
```
The application will launch automatically in your web browser at `http://localhost:8501`.
