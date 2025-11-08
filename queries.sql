-- 1. Movie with the highest average rating
SELECT m.title, AVG(r.rating) AS avg_rating
FROM movies m
JOIN ratings r ON m.movie_id = r.movie_id
GROUP BY m.movie_id
ORDER BY avg_rating DESC
LIMIT 1;

-- 2. Top 5 genres with the highest average rating
SELECT m.genres, AVG(r.rating) AS avg_rating
FROM movies m
JOIN ratings r ON m.movie_id = r.movie_id
GROUP BY m.genres
ORDER BY avg_rating DESC
LIMIT 5;

-- 3. Director with the most movies
SELECT director, COUNT(*) AS movie_count
FROM movies
WHERE director IS NOT NULL
GROUP BY director
ORDER BY movie_count DESC
LIMIT 1;

-- 4. Average rating per year (from movie title)
SELECT year, COUNT(*) AS total_movies
FROM movies
WHERE year IS NOT NULL
GROUP BY year
ORDER BY year;



