-- list all shows in database
-- records with genre linked are not displayed
-- records in ascending order by tv_shows.title and tv_show_genres.genre_id
-- database name will be passed as mysql argument
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.show_id IS NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id;

