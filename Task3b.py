import pandas as pd
from pandasql import sqldf

movies = pd.DataFrame(pd.read_csv("movies.csv"))
tags =  pd.DataFrame(pd.read_csv("tags.csv"))
Question_3a = pd.DataFrame(pd.read_csv("Question_3a.csv"))

def enhanced_similar_movie_sql(id):
    query = """ select movieId, title from movies where movieid in (
            select DISTINCT(id_tags) from
            (select movieId as id_tags from tags where tag in
            (select tag from tags where movieid = {id})) as t

            inner join 

            (SELECT movieId as id_similar from Question_3a) as s
            on t.id_tags = s.id_similar
            where id_tags is not {id});""".format(id = id)
    return sqldf(query)        

print("Enhanced similar movies are : ")
enhanced_similar_movie_sql_res = enhanced_similar_movie_sql(150)   
print(enhanced_similar_movie_sql_res) 