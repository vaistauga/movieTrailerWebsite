import fresh_tomatoes
import mediaDataBase

#Grab the media from the mediaDatabase.py
MOVIES = [
    mediaDataBase.INCEPTION,
    mediaDataBase.INTERSTELLAR,
    mediaDataBase.BURN_AFTER_READING,
    mediaDataBase.FARGO,
    mediaDataBase.BATMAN_VS_SUPERMAN,
    mediaDataBase.SUCKER_PUNCH,]

fresh_tomatoes.open_movies_page(MOVIES)
