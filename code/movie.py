from tmdbv3api import Movie, TMDb
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')


def start_tmdb():

    tmdb = TMDb()
    tmdb.api_key = API_KEY
    tmdb.language = 'pt'
    tmdb.debug = True

    movie = Movie()

    popular = movie.popular()

    for p in popular:
        # print(p.id)
        print(p.title)


def input_movie() -> list:
    movie_list = []

    movie_input = input('Tell me a movie:\n')
    movie_list.append(movie_input)

    return movie_list