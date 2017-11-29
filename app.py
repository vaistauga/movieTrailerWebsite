import fresh_tomatoes
import mediaDataBase

def showSamplePage():
    '''Generates and open a webpage showing Vai's favorite movies'''
    #Grab the media from the mediaDatabase.py
    movies = [
        mediaDataBase.INCEPTION,
        mediaDataBase.INTERSTELLAR,
        mediaDataBase.BURN_AFTER_READING,
        mediaDataBase.FARGO,
        mediaDataBase.BATMAN_VS_SUPERMAN,
        mediaDataBase.SUCKER_PUNCH,]

    fresh_tomatoes.open_movies_page(movies)
