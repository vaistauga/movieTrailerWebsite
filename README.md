# Movie-Trailer-Project

## overview
The purpose of the project is to demonstrates the use of a Python to generate a static webpage.  
Python code pulls data (title, image, etc.) about the movies from python class,translates it into a webpage, and opens it in a browser.  
The webpage displays a visual grid of my favorite movies.  Each cell of the grid contains a title and a visual.  User may click the cell to bring up a YouTube video which plays the movie trailer.

I've built this during [Udacity's full-stack nanodegree program](https://www.udacity.com/nanodegree). 

## Demo
[You may see an example of precomiled website here]().

## Usage
### Generate static website which contains a preset list of movies
1. Import app.py module, 
2. Run it.

### Create your own list of movies, then use python to show them in a website
1. Import MediaTypes.py
3. Create an array of movie objects.  Movie objects can be created by calling media.Movie() function that takes following paramters:
    1. Title 
    1. Year
    1. Poster URL
    1. Trailer URL - must be Youtube
4. Import fresh_tomatoes.py
5. Lastly, fresh_tomatoes.open_movies_page() which takes your array of movies as a paramter.

Following is an example of what the steps above could look like
```
import media
import fresh_tomatoes

#Create movie object 1
INCEPTION = mediaTypes.Video(
    "Inception",
    "Go into the dreams of a bussinessman to change his mind about something",
    "https://images-na.ssl-images-amazon            com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
    "https://www.youtube.com/watch?v=66TuSJo4dZM")

#Create movie object 2
INTERSTELLAR = mediaTypes.Video(
    "Intersellar",
    "Travel through the black hole to save humanity",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BZjdkOTU3MDktN2IxOS00OGEyLWFmMjktY2FiMmZkNWIyODZiXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_SY1000_SX675_AL_.jpg",
    "https://www.youtube.com/watch?v=0vxOhd4qlnA")

# Create movie trailer page with array of one movie
fresh_tomatoes.open_movies_page([INCEPTION, INTERSTELLAR])
```

## Copyright and License
* Project starter code (supplied without rights information) contributed by [Udacity](http://www.udacity.com).
*  Additional code contributed by [Vaidotas Staugaitis]() is offered under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/).
