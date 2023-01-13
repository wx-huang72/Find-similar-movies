-- find out the maximum number of genres, which is max(occurrences) = 10
SELECT MAX(LENGTH(genres) - length(REPLACE(genres, '|', ''))) + 1 AS max_occurrences FROM movies;

-- create a empty table to save the result
Drop table if EXISTS movie_genres_new;
CREATE TABLE if not exists movie_genres_new (movieId INTEGER, genre VARCHAR(20));

 -- single genre selected
Insert into movie_genres_new
SELECT movieid, genres FROM movies where genres not like '%|%'; 

-- multiple genres selected
Drop table if EXISTS new_1;
CREATE TABLE if NOT EXISTS new_1 (movieId INTEGER, FirstStr TEXT, other TEXT);

INSERT INTO new_1 
select movieId,  SUBSTR(genres, 0, CHARINDEX('|', genres)) AS FirstStr,
SUBSTR(genres, CHARINDEX('|', genres)+1,  length(genres)-CHARINDEX('|', genres) ) as other
FROM movies where genres like '%|%';

insert into movie_genres_new
select movieId, firststr
from new_1;

insert into movie_genres_new
select movieId, other
from new_1 where other not like '%|%';

drop table if EXISTS new_2;
CREATE TABLE if not exists new_2 (movieId INTEGER, SecondStr TEXT, other TEXT);

INSERT INTO new_2
select movieId,SUBSTR(other, 0, CHARINDEX('|', other)) AS SecondStr,
SUBSTR(other, CHARINDEX('|', other)+1,  length(other)-CHARINDEX('|', other) ) as other
FROM new_1 where other like '%|%';

insert into movie_genres_new
select movieId, secondstr
from new_2;

insert into movie_genres_new
select movieId, other
from new_2 where other not like '%|%';

drop table if EXISTS new_3;
CREATE TABLE if not EXISTS new_3 (movieId INTEGER, ThirdStr TEXT, other TEXT);

INSERT INTO new_3
select movieId,SUBSTR(other, 0, CHARINDEX('|', other)) AS ThirdStr,
SUBSTR(other, CHARINDEX('|', other)+1,  length(other)-CHARINDEX('|', other) ) as other
FROM new_2 where other like '%|%';

insert into movie_genres_new
select movieId, thirdstr
from new_3;

insert into movie_genres_new
select movieId, other
from new_3 where other not like '%|%';

drop table if EXISTS new_4;
CREATE TABLE if not EXISTS new_4 (movieId INTEGER, ForthStr TEXT, other TEXT);

INSERT INTO new_4
select movieId,SUBSTR(other, 0, CHARINDEX('|', other)) AS ForthStr,
SUBSTR(other, CHARINDEX('|', other)+1,  length(other)-CHARINDEX('|', other) ) as other
FROM new_3 where other like '%|%';

insert into movie_genres_new
select movieId, forthstr
from new_4;

insert into movie_genres_new
select movieId, other
from new_4 where other not like '%|%';

drop table if EXISTS new_5;
CREATE TABLE if not EXISTS new_5 (movieId INTEGER, FifthStr TEXT, other TEXT);

INSERT INTO new_5
select movieId,SUBSTR(other, 0, CHARINDEX('|', other)) AS FifthStr,
SUBSTR(other, CHARINDEX('|', other)+1,  length(other)-CHARINDEX('|', other) ) as other
FROM new_4 where other like '%|%';

insert into movie_genres_new
select movieId, fifthstr
from new_5;

insert into movie_genres_new
select movieId, other
from new_5 where other not like '%|%';

drop table if EXISTS new_6;
CREATE TABLE if not EXISTS new_6 (movieId INTEGER, SixthStr TEXT, other TEXT);

INSERT INTO new_6
select movieId,SUBSTR(other, 0, CHARINDEX('|', other)) AS SixthStr,
SUBSTR(other, CHARINDEX('|', other)+1,  length(other)-CHARINDEX('|', other) ) as other
FROM new_5 where other like '%|%';

insert into movie_genres_new
select movieId, sixthstr
from new_6;

insert into movie_genres_new
select movieId, other
from new_6 where other not like '%|%';

drop table if EXISTS new_7;
CREATE TABLE if not EXISTS new_7 (movieId INTEGER, SeventhStr TEXT, other TEXT);

INSERT INTO new_7
select movieId,SUBSTR(other, 0, CHARINDEX('|', other)) AS SeventhStr,
SUBSTR(other, CHARINDEX('|', other)+1,  length(other)-CHARINDEX('|', other) ) as other
FROM new_6 where other like '%|%';

insert into movie_genres_new
select movieId, SeventhStr
from new_7;

insert into movie_genres_new
select movieId, other
from new_7 where other not like '%|%';

drop table if EXISTS new_8;
CREATE TABLE if not EXISTS new_8 (movieId INTEGER, EighthStr TEXT, other TEXT);

INSERT INTO new_8
select movieId,SUBSTR(other, 0, CHARINDEX('|', other)) AS EighthStr,
SUBSTR(other, CHARINDEX('|', other)+1,  length(other)-CHARINDEX('|', other) ) as other
FROM new_7 where other like '%|%';

insert into movie_genres_new
select movieId, EighthStr
from new_8;

insert into movie_genres_new
select movieId, other
from new_8 where other not like '%|%';

drop table if EXISTS new_9;
CREATE TABLE if not EXISTS new_9 (movieId INTEGER, NinthStr TEXT, last TEXT);

INSERT INTO new_9
select movieId,SUBSTR(other, 0, CHARINDEX('|', other)) AS NinthStr,
SUBSTR(other, CHARINDEX('|', other)+1,  length(other)-CHARINDEX('|', other) ) as last
FROM new_8 where other like '%|%';

insert into movie_genres_new
select movieId, NinthStr
from new_9;

insert into movie_genres_new
select movieId, last
from new_9 ;