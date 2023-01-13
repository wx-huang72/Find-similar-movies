import pandas as pd
from pandasql import sqldf

movies = pd.DataFrame(pd.read_csv("movies.csv"))
genres = pd.DataFrame(pd.read_csv("genres.csv"))
ratings = pd.DataFrame(pd.read_csv("ratings.csv"))

def similar_movie_sql(id):
    query = """
            select movieId, title from movies where movieid in (
            SELECT DISTINCT(id_genres) FROM
              -- at least one genre common
            (SELECT movieid as id_genres from genres where genre in (
            SELECT genre from genres where movieid = 150)) as g
            inner join 
              -- at least one rating common
            (select movieid as id_ratings from ratings where rating in (
            select rating from ratings where movieid = 150)) as r
            on g.id_genres = r.id_ratings
            where id_genres is not 150);;""".format(id = id)
    return sqldf(query)

print("Similar movies are: ")
similar_movie_sql_res = similar_movie_sql(150)
print(similar_movie_sql_res)