import pandas as pd
import requests
from sqlalchemy import create_engine, text
import sqlite3
import os
import time

# ---------------------------
# CONFIGURATION
# ---------------------------
OMDB_API_KEY = "982d0fb2"  
DATABASE_FILE = "movies.db"
DATA_PATH = "data"

# ---------------------------
# SETUP DATABASE CONNECTION
# ---------------------------
engine = create_engine(f"sqlite:///{DATABASE_FILE}")

# ---------------------------
# 1. EXTRACT
# ---------------------------
movies_path = os.path.join(DATA_PATH, "movies.csv")
ratings_path = os.path.join(DATA_PATH, "ratings.csv")

movies = pd.read_csv(movies_path)
ratings = pd.read_csv(ratings_path)

print(f"✅ Loaded {len(movies)} movies and {len(ratings)} ratings")

# ---------------------------
# 2. TRANSFORM (Clean + Rename Columns)
# ---------------------------
# Match CSV column names with SQL schema
movies.rename(columns={'movieId': 'movie_id'}, inplace=True)
ratings.rename(columns={'movieId': 'movie_id', 'userId': 'user_id'}, inplace=True)

# Extract year from title before cleaning it
movies['year'] = movies['title'].str.extract(r'\((\d{4})\)')
# Clean title (remove year part)
movies['title'] = movies['title'].str.replace(r'\s\(\d{4}\)', '', regex=True)
movies.drop_duplicates(subset=['title'], inplace=True)

# ---------------------------
# 3. ENRICH (OMDb API)
# ---------------------------
def fetch_movie_details(title):
    """Fetch movie details from OMDb API using movie title."""
    if OMDB_API_KEY == "your_api_key_here" or not OMDB_API_KEY.strip():
        # Skip API calls if no key provided
        return pd.Series([None, None])

    try:
        url = f"http://www.omdbapi.com/?t={title}&apikey={OMDB_API_KEY}"
        response = requests.get(url, timeout=5).json()
        if response.get('Response') == 'True':
            return pd.Series([response.get('Director'), response.get('BoxOffice')])
        else:
            return pd.Series([None, None])
    except Exception as e:
        print(f"⚠️ API error for '{title}': {e}")
        return pd.Series([None, None])

# Limit enrichment to 20 movies (free tier API)
sampled_movies = movies.head(100).copy()  
sampled_movies[['director', 'box_office']] = sampled_movies['title'].apply(fetch_movie_details)
time.sleep(1)

# Merge enrichment data back
movies = movies.merge(sampled_movies[['title', 'director', 'box_office']], on='title', how='left')

print("✅ Enriched movie data with API details")

# ---------------------------
# 4. LOAD (Create / Replace Tables)
# ---------------------------
with sqlite3.connect(DATABASE_FILE) as conn:
    # Drop old tables if they exist
    conn.execute("DROP TABLE IF EXISTS movies;")
    conn.execute("DROP TABLE IF EXISTS ratings;")
    
    # Run schema creation
    with open("schema.sql", "r") as f:
        conn.executescript(f.read())

    # Load cleaned data
    movies.to_sql('movies', conn, if_exists='append', index=False)
    ratings.to_sql('ratings', conn, if_exists='append', index=False)

print("✅ Data successfully loaded into SQLite database")

# ---------------------------
# 5. VALIDATION
# ---------------------------
with engine.connect() as conn:
    movie_count = conn.execute(text("SELECT COUNT(*) FROM movies")).fetchone()[0]
    rating_count = conn.execute(text("SELECT COUNT(*) FROM ratings")).fetchone()[0]

print(f"📊 Movies in DB: {movie_count}")
print(f"📊 Ratings in DB: {rating_count}")
print("🎉 ETL process completed successfully!")
