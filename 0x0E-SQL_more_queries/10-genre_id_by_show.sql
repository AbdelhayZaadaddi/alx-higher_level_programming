-- LIST ALL SHOWS CONTAINED IN hbtn_0d_tvshows
-- tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
SELECT tv_shows.title, tv_show_genres_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;