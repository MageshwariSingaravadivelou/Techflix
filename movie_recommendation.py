from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

eng_movies = pd.read_excel(r'./model/eng_movies.xlsx')

# Calculate mean of vote average column
C = eng_movies['vote_average'].mean()
print(C)

# Calculate the minimum number of votes required to be in the chart, m
m = eng_movies['vote_count'].quantile(0.07)
print(m)

# Filter out all qualified movies into a new DataFrame
q_movies = eng_movies.copy().loc[eng_movies['vote_count'] >= m]

# Function that computes the weighted rating of each movie
def weighted_rating(x, m=m, C=C):
    v = x['vote_count']
    R = x['vote_average']

    # Calculation based on the IMDB formula
    return (v/(v+m) * R) + (m/(m+v) * C)

# Define a new feature 'score' and calculate its value with `weighted_rating()`
q_movies['score'] = q_movies.apply(weighted_rating, axis=1)
q_movies['score'] = q_movies['score'].round(decimals=2)

count_vectorizer = CountVectorizer(stop_words="english")
count_matrix = count_vectorizer.fit_transform(q_movies["soup"])
print(count_matrix.shape)

cosine_sim2 = cosine_similarity(count_matrix, count_matrix) 
print(cosine_sim2.shape)

q_movies = q_movies.reset_index()
q_movies['title_'] = q_movies['title'].str.lower()
indices = pd.Series(q_movies.index, index=q_movies["title_"]).drop_duplicates()

def get_recommendations(title):
    cosine_sim = cosine_sim2
    title_ = title.lower()
    idx = indices[title_]
    similarity_scores = list(enumerate(cosine_sim[idx]))
    similarity_scores= sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    similarity_scores= similarity_scores[1:4]


    movies_indices = [ind[0] for ind in similarity_scores]

    # remove the input movie name from the list
    # Get names of indexes for which column Age has value 30
    indexNames = q_movies[ q_movies['title_'] == title_ ].index
    print(indexNames)
    # Delete these row indexes from dataFrame
    q_movies.drop(indexNames, inplace=True)
    # movies_list = q_movies[q_movies["title_"].str.contains(title_)==False]

    movies = q_movies["title"].iloc[movies_indices]
    release_date = q_movies['release_date'].iloc[movies_indices]
    genres = q_movies['genres_'].iloc[movies_indices]
    tag_line = q_movies['tagline'].iloc[movies_indices]
    score = q_movies['score'].iloc[movies_indices]

    return_df = pd.DataFrame(columns=['Title','TagLine', 'Genres', 'Year', 'Score'])
    return_df['Title'] = movies
    return_df['TagLine'] = tag_line
    return_df['Genres'] = genres
    return_df['Year'] = release_date
    return_df['Score'] = score
    print(return_df)
    
    return return_df.sort_values(by='Score', ascending=False)
