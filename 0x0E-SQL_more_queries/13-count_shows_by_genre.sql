-- script counts tv shows by genre
-- genres without links are not counted
-- result is sorted in descending order by number of shows
-- database name is passed as mysql argument
SELECT tv_genres.name AS genre, count(tv_show_genres.genre_id) AS number_of_shows
FROM tv_genres INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;

