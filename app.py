import fresh_tomatoes
import mediaDataBase


def showSamplePage():
    # Generates HTML with a preset list of movies and opens it in a browser.

    # Grab the media from the mediaDatabase.py
    movies = [
        mediaDataBase.INCEPTION,
        mediaDataBase.INTERSTELLAR,
        mediaDataBase.BURN_AFTER_READING,
        mediaDataBase.FARGO,
        mediaDataBase.SUCKER_PUNCH, ]

    fresh_tomatoes.open_movies_page(movies)
