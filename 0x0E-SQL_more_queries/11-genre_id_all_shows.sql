-- Reading records for titles and genre id, which are sorted
-- in ascending order. If a show doesn't have a genre, display NULL.
SELECT tv_shows.title as title, tv_show_genres.genre_id as genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY title, genre_id;
