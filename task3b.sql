--trying to find similar movies of movieid = 150
drop table if EXISTS Question_3b;
create table if not EXISTS Question_3b (movieId INTEGER,title TEXT);

insert into Question_3b
select movieId, title from movies where movieid in (
select DISTINCT(id_tags) from
(select movieId as id_tags from tags where tag in
(select tag from tags where movieid = 150)) as t

inner join 

(SELECT movieId as id_similar from Question_3a) as s
on t.id_tags = s.id_similar
where id_tags is not 150);