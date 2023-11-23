-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.genre_id) AS 'number_of_shows'
FROM tv_genres RIGHT JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id 
GROUP BY genre ORDER BY number_of_shows DESC;
