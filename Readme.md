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

