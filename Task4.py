import pandas as pd
movies = pd.read_csv("movies.csv")
tags = pd.read_csv("tags.csv")
ratings = pd.read_csv("ratings.csv")
genres = pd.read_csv("genres.csv")
Question_1b = pd.read_csv("Question_1b.csv")
Question_1c = pd.read_csv("Question_1c.csv")
Question_3a = pd.read_csv("Question_3a.csv")
Question_3b = pd.read_csv("Question_3b.csv")

# Test Case 1 -- Task 1(a) 
## choose random numbers as movieId from both ratings.csv and tags.csv files, we expect this movieId also shows up movies.csv files,
## to prove that we have filtered out rows from ratings.csv and tags.csv which is not related to movies.csv
random_id1 = 6534       # ratings
random_id2 = 1569       # tags

if all(x in movies["movieId"].tolist() for x in [random_id1,random_id2]):
    print("Test Case 1 Succeeds. ")
else:
    print("Test Case 1 Fails. ")  

# # We will perfrom 4 tests on task 1 question (b), they are
# # 1> at least one common genre and one identical rating ==> supposed to show up in the result list
# # 2> at least one common genre, but no identical rating ==> not supposed to show up in the result list
# # 3> at least one identical rating, but no common genre ==> not supposed to show up in the result list
# # 4> Neither gnere nor rating is the same               ==> not supposed to show up in the result list

# Test Case 2 -- Task 1(b) - 1>
search_id3 = 68157      
if search_id3 in Question_1b["movieId"].tolist():
    print("Test Case 2 Succeeds. ")
else:
    print("Test Case 2 Fails. ")

# Test Case 3 -- Task 1(b) - 2>
search_id4 = 92681
if search_id4 not in Question_1b["movieId"].tolist():
    print("Test Case 3 Succeeds. ")
else:
    print("Test Case 3 Fails. ")

# Test Case 4 -- Task 1(b) - 3>
search_id5 = 3287
if search_id5 not in Question_1b["movieId"].tolist():
    print("Test Case 4 Succeeds. ")
else:
    print("Test Case 4 Fails. ")

# Test Case 5 -- Task 1(b) - 4>
search_id6 = 3604
if search_id6 not in Question_1b["movieId"].tolist():
    print("Test Case 5 Succeeds. ")
else:
    print("Test Case 5 Fails. ")

# # We will perfrom 2 tests on task 1 question (c), they are
# # 1> at least one tag identical ==> supposed to show up in the result list
# # 2> no identical tags          ==> not supposed to show up in the result list

# Test Case 6 -- Task 1(c) - 1>
search_id7 = 1223
if search_id7 in Question_1c["movieId"].tolist():
    print("Test Case 6 Succeeds. ")
else:
    print("Test Case 6 Fails. ")

# Test Case 7 -- Task 1(c) - 2>
search_id8= 106782
if search_id8 not in Question_1c["movieId"].tolist():
    print("Test Case 7 Succeeds. ")
else:
    print("Test Case 7 Fails. ")

# Test Case 8 -- Task 2
search_id9 = 4628
actual_values = genres[genres['movieId'] == search_id9].loc[:, 'genre'].values[0].split("|").sort()        
expected_values = movies[movies['movieId'] == search_id9].loc[:, 'genres'].values[0].split("|").sort()
if actual_values == expected_values:
    print("Test Case 8 Succeeds. ")
else:    
    print("Test Case 8 fails. ")

# # Since 3(a) and 1(b) solve the same problem, as well as question 3(b) and 1(c), they will be tested under the same variety of conditions    

# Test Case 9 -- Task 3(a) - 1>
search_id10 = 3266
if search_id10 in Question_3a["movieId"].tolist():
    print("Test Case 9 Succeeds. ")
else:
    print("Test Case 9 Fails. ")

# Test Case 10 -- Task 3(a) - 2>
search_id11 = 806
if search_id11 not in Question_3a["movieId"].tolist():
    print("Test Case 10 Succeeds. ")
else:
    print("Test Case 10 Fails. ")

# Test Case 11 -- Task 3(a) - 3>
search_id12 = 2779
if search_id12 not in Question_3a["movieId"].tolist():
    print("Test Case 11 Succeeds. ")
else:
    print("Test Case 11 Fails. ")

# Test Case 12 -- Task 3(a) - 4>
search_id13 = 64969
if search_id13 not in Question_3a["movieId"].tolist():
    print("Test Case 12 Succeeds. ")
else:
    print("Test Case 12 Fails. ")  

# Test Case 13 -- Task 3(b) - 1>
search_id14 = 924
if search_id14 in Question_3b["movieId"].tolist():
    print("Test Case 13 Succeeds. ")
else:
    print("Test Case 13 Fails. ")

# Test Case 14 -- Task 3(b) - 2>
search_id15= 27706
if search_id15 not in Question_3b["movieId"].tolist():
    print("Test Case 14 Succeeds. ")
else:
    print("Test Case 14 Fails. ")