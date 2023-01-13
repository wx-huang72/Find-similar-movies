import pandas as pd

# Question a) Import
## import the dataset into dataframes
movies = pd.read_csv("movies.csv")
tags = pd.read_csv("tags.csv")
ratings = pd.read_csv("ratings.csv")

movies_df = pd.DataFrame(movies)
tags_df = pd.DataFrame(tags)
ratings_df = pd.DataFrame(ratings)

## drop duplicates
movies_df.drop_duplicates()
tags_df.drop_duplicates()
ratings_df.drop_duplicates()

## filter rows containing blanks
movies_df.dropna()
tags_df.dropna()
ratings_df.dropna()

## filter out rows from ratings.csv and tags.csv which pertain to movies that are *not* present in movies.csv
movies_movieId = movies_df["movieId"].tolist()

for index_t, t in tags_df.iterrows():
    if t['movieId'] not in movies_movieId:
        tags_df.drop(index_t,inplace=True)

for index_r, r in ratings_df.iterrows():
    if r['movieId'] not in movies_movieId:
        ratings_df.drop(index_r,inplace=True)   

# Question b) Similar Movies Retrieval

def similar_movie(x):
    """
    input: x, a movie id
    return: all movies that have at least one genre common and at least one ratings common with x
    """
    genre = movies_df[movies_df['movieId'] == x].loc[:, 'genres']
    each_genre = genre.values.item(0).split("|")                #list of genres
    rating = ratings_df[ratings_df['movieId'] == x].loc[:,'rating']

    movie_res = pd.DataFrame(columns = ['movieId', 'title'])
    rating_res = pd.DataFrame(columns = ['movieId'])

    for index_m, row_m in movies_df.iterrows():
        if (any(x in each_genre for x in row_m['genres'].split("|"))):
            movie_res = movie_res.append({'movieId': row_m['movieId'], 'title': row_m['title']}, ignore_index = True)
    
    for index_r, row_r in ratings_df.iterrows():
        if (row_r['rating'] in rating.values):
            rating_res = rating_res.append({'movieId': row_r['movieId']},ignore_index = True)

    res = pd.merge(movie_res, rating_res, on = 'movieId', how = 'inner')        # inner join of both
    res = res.drop_duplicates()
    res.drop(res.loc[res['movieId'] == x].index, inplace= True)                 # remove the movie id you type in as a parameter from the result
    return res.reset_index(drop=True)


print('Similar movies are: \n')      
similar_movie_res = similar_movie(150)
print(similar_movie_res)                                                        # you can choose either to print it out or to save it as a file
# similar_movie_res.to_csv("Question_1b.csv")
# print("Question 1 b) saved! ")

# Question c) Enhancing Similar Movies Retrieval

def enhancing_similar_movie(df, x):
    """
    input df: a dataframe contains movies which have been filtered by genres and ratings
    input x: given movie id
    return: a dataframe contains movies which also been filtered by tags
    """
    tag = tags_df[tags_df['movieId'] == x].loc[:,'tag']
    tag_res = pd.DataFrame(columns = ['movieId'])

    for index_t, row_t in tags_df.iterrows():
        if (row_t['tag'] in tag.values):
            tag_res = tag_res.append({'movieId': row_t['movieId']}, ignore_index = True)

    enhance_res = pd.merge(df, tag_res, on = 'movieId', how = 'inner')
    enhance_res = enhance_res.drop_duplicates()
    enhance_res.drop(enhance_res.loc[enhance_res['movieId'] == x].index, inplace=True)
    return enhance_res.reset_index(drop=True)
    

print('Enhancing similar movies are: \n')
enhance_similar_movie_res = enhancing_similar_movie(similar_movie_res,150)
print(enhance_similar_movie_res)
# enhance_similar_movie_res.to_csv('Question_1c.csv')
# print("Question 1 c) saved! ")
