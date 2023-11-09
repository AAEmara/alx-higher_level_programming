-- Reading title and genre_id from `hbtn_0d_tvshows` database.
-- Shows don't have any genre linked and sorted in ascending order.
SELECT tv_shows.title AS title, tv_show_genres.genre_id AS genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
WHERE genre_id IS NULL
ORDER BY title, genre_id ASC
