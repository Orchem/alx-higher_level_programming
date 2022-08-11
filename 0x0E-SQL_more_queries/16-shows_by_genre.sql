-- script list all shows and all genres linked to that show
-- shows with null genre are displayed
-- database name will be passed as mysql argument
SELECT tv_shows.title AS title, tv_genres.name AS name FROM tv_shows
LEFT OUTER JOIN tv_show_genres tsg ON tv_shows.id = tsg.show_id
LEFT OUTER JOIN tv_genres ON tv_genres.id = tsg.genre_id
ORDER BY title, name;

