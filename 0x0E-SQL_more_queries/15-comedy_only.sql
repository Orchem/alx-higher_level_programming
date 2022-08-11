-- script lists all comedy shows
-- database name is passed as mysql argument
SELECT tv_shows.title AS title FROM tv_shows inner
JOIN tv_show_genres tsg ON tv_shows.id = tsg.show_id
INNER JOIN tv_genres tg ON tg.id = tsg.genre_id
WHERE tg.name = 'Comedy'
ORDER BY title;

