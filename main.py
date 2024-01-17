import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

movies = pd.read_csv("./data/movie.csv")
# print(movies.head())
# print(movies.shape)
# print(movies.columns)
# print(movies.dtypes)
# print(movies.describe())
# print(movies.isnull().sum())
# print(movies['genres'].unique())

# Split the 'genres' column into a list of genres
movies['genres'] = movies['genres'].apply(lambda x: x.split('|'))

# One-hot encoding
for genre in set(genre for sublist in movies['genres'] for genre in sublist):
    movies[genre] = movies['genres'].apply(lambda x: 1 if genre in x else 0)

# Now, movies has additional columns for each genre
# print(movies.head())

genre_matrix = movies.drop(['movieId', 'title', 'genres'], axis=1)
# NxN matrix, i and j
cosine_sim = cosine_similarity(genre_matrix)

def get_recs(movie_title, cosine_sim, movies):
    # gets index of requested movie in movies dataframe
    idx = movies.index[movies['title'] == movie_title].tolist()[0]

    # returns list of sim scores for idx'th row (for requested movie)
    sim_scores = list(enumerate(cosine_sim[idx]))
    
    # sorts sim scores based on sim score
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # gets indexes based on sim score, excluding requested movie
    movie_indices = [i[0] for i in sim_scores if i[0] != idx]

    # gets top ten most similar movies
    movie_indices = movie_indices[:10]

    return movies['title'].iloc[movie_indices]

result = get_recs(movie_title="Little Women (2019)", cosine_sim=cosine_sim, movies=movies)
print(result)
