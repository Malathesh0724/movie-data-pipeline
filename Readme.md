# 🎥 Movie Data Pipeline (Data Engineering Project)

A simple **ETL pipeline** built with **Python**, **Pandas**, and **SQLite**, designed to ingest, transform, enrich, and analyze movie data.  
This project is created as part of a **Data Engineering assignment** and demonstrates practical data pipeline design and SQL-based analysis.

---

## 🚀 Project Overview

The goal of this project is to:
1. **Extract** movie and rating data from CSV files (MovieLens dataset).  
2. **Transform** the data — clean titles, extract release years, handle missing values.  
3. **Enrich** the dataset with additional details (Director, Box Office) from the **OMDb API**.  
4. **Load** the final, structured data into an **SQLite database**.  
5. **Analyze** insights using SQL queries.

---

## 🧱 Project Structure

movie-data-pipeline/
├── etl.py # Python script for Extract, Transform, Load
├── schema.sql # Database schema (CREATE TABLE statements)
├── queries.sql # Analytical SQL queries
├── requirements.txt # Required Python libraries
├── README.md # Project documentation
└── data/
├── movies.csv # Input movie data (MovieLens)
└── ratings.csv # Input ratings data (MovieLens)


---

## 🧩 How It Works

### 🔹 1. Extract
Reads movie and rating data from the **MovieLens Small Dataset**:
- `movies.csv`
- `ratings.csv`

### 🔹 2. Transform
- Cleans movie titles.
- Extracts **release year** from the title.
- Renames columns to match SQL schema (`movieId → movie_id`, `userId → user_id`).

### 🔹 3. Enrich (via OMDb API)
For a sample of movies (default 20), the script fetches:
- **Director**
- **Box Office Collection**

You can increase the limit safely if you have a valid API key.

### 🔹 4. Load
The cleaned and enriched data is stored in an **SQLite database** (`movies.db`).

### 🔹 5. Analyze
Run SQL queries from `queries.sql` to answer questions such as:
- Which movie has the highest average rating?
- What are the top 5 genres with the best ratings?
- Who is the most frequent director?
- What is the average rating of movies released each year?

---

## 🛠️ Setup Instructions

### Prerequisites
- Python 3.8 or later
- pip (Python package manager)

#### Create and Activate Virtual Environment
python -m venv venv
venv\Scripts\activate          # On Windows

### Install Dependencies

pip install -r requirements.txt

Download Dataset

Download the MovieLens Small Dataset and place the following files inside the data/ folder:
movies.csv
ratings.csv

#### Set Up OMDb API Key

Sign up for a free key at http://www.omdbapi.com/  Then, update your key in the etl.py file:

OMDB_API_KEY = "your_api_key_here"

### Run the Pipeline

python etl.py

This script will:
Clean and enrich the data.
Create an SQLite database (movies.db).
Load the transformed data into tables.

#### Run SQL Queries

After the database is created, open it in DB Browser for SQLite and execute queries from queries.sql to answer:
1.Movie with highest average rating
2.Top 5 genres with highest average rating
3.Director with most movies
4.Average rating of movies released each year

#### Design Choices & Assumptions

SQLite was chosen for simplicity, portability, and ease of use in local environments.

Pandas was used for fast data manipulation and cleaning.

SQLAlchemy enables database connection and writing to tables easily.

API enrichment is limited to the first 20 movies to stay within the free OMDb API tier.

Assumed that all CSVs are clean and have standard MovieLens formatting.

ETL script is idempotent — running it again overwrites tables safely.

Challenges Faced & How They Were Overcome
Challenge	Solution
Handling column mismatches (movieId, userId)	Renamed columns using Pandas to match SQL schema.
Missing or unmatched OMDb data	Implemented checks to skip missing titles and avoid API crashes.
API limits for free OMDb key	Restricted enrichment to top 20 movies for demo; scalable for paid plan.
SQLite “database locked” errors during reruns	Ensured connections are closed and added logic to recreate DB cleanly.
Extracting movie release years	Used regex extraction before title cleaning for accuracy.



