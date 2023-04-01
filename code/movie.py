import imdb

ia = imdb.Cinemagoer()

movie_list = []


movies = ia.search_movie(input('Movie name: '))
movie_list.append(movies)
title = movies[0]['title']
director = movies['directors']
genres = movies['genres']
