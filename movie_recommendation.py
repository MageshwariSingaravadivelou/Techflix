from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

eng_movies = pd.read_excel(r'../model/eng_movies.xlsx')

count_vectorizer = CountVectorizer(stop_words="english")
count_matrix = count_vectorizer.fit_transform(eng_movies["soup"])
print(count_matrix.shape)

cosine_sim2 = cosine_similarity(count_matrix, count_matrix) 
print(cosine_sim2.shape)

eng_movies = eng_movies.reset_index()
indices = pd.Series(eng_movies.index, index=eng_movies["title"]).drop_duplicates()

def get_recommendations(title):
    cosine_sim = cosine_sim2
    idx = indices[title]
    similarity_scores = list(enumerate(cosine_sim[idx]))
    similarity_scores= sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    similarity_scores= similarity_scores[1:4]


    movies_indices = [ind[0] for ind in similarity_scores]
    movies = eng_movies["title"].iloc[movies_indices]
    release_date = eng_movies['release_date'].iloc[movies_indices]
    genres = eng_movies['genres_'].iloc[movies_indices]
    tag_line = eng_movies['tagline'].iloc[movies_indices]
    return_df = pd.DataFrame(columns=['Title','TagLine', 'Genres', 'Year'])
    return_df['Title'] = movies
    return_df['TagLine'] = tag_line
    return_df['Genres'] = genres
    return_df['Year'] = release_date
    
    return return_df
