CREATE TABLE IF NOT EXISTS movies (
    movie_id INTEGER PRIMARY KEY,
    title TEXT,
    genres TEXT,
    year TEXT,         
    director TEXT,
    box_office TEXT
);


CREATE TABLE IF NOT EXISTS ratings (
    rating_id INTEGER PRIMARY KEY AUTOINCREMENT,
    movie_id INTEGER,
    user_id INTEGER,
    rating REAL,
    timestamp TEXT,
    FOREIGN KEY (movie_id) REFERENCES movies (movie_id)
);

