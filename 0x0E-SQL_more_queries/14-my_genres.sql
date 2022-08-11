-- script list all genres of the show Dexter
-- database name is passed as argument of mysql
SELECT tv_genres.name AS name FROM tv_genres
INNER JOIN tv_show_genres tvg ON tv_genres.id = tvg.genre_id
INNER JOIN tv_shows ts ON tvg.show_id = ts.id
WHERE ts.title = 'Dexter'
ORDER BY name;

