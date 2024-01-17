# movie-recs

## what is this?
this is a simple program that 10 similar movies in the movielens dataset to the one inputed by the user. the algorithm utilizes cosine simliarity to find movies that have the closest matches in genres to the one inputted by the user and returns them.


## to run locally
1. install scikit-learn: pip install scikit-learn
2. install pandas: pip install pandas
3. download the movielens dataset and place in root folder, calling the data folder "data": https://www.kaggle.com/datasets/grouplens/movielens-20m-dataset?resource=download

## to use
simply control f the movie.csv file in the data folder and search for a movie you're interested in. copy the exact name of this movie (including the year) and replace the movie_title parameter when calling get_rec in main.py with your movie.
