-- at least one genre common and one rating common
-- trying to find similar movies of movieid = 150
drop table if EXISTS Question_3a;
create table if not EXISTS Question_3a (movieId INTEGER, title TEXT);

insert into Question_3a
select movieId, title from movies where movieid in (

SELECT DISTINCT(id_genres) FROM   -- remove duplicates
  
  -- at least one genre common
(SELECT movieid as id_genres from genres where genre in (
SELECT genre from genres where movieid = 150)) as g

inner join 
  
  -- at least one rating common
(select movieid as id_ratings from ratings where rating in (
select rating from ratings where movieid = 150)) as r
  
on g.id_genres = r.id_ratings

where id_genres is not 150);
