# Movie-Trailer-Project

## overview
I've built this during [Udacity's full-stack nanodegree program](https://www.udacity.com/nanodegree). 

The purpose of this project is to demonstrate the use of a Python to generate a static webpage.  
Python code pulls data which discribes my favorite (title, image, etc.) from a class, populates HTML template with it, and opens it in a browser.
The generated webpage displays a grid of my favorite movies.  Each cell of the grid contains a title and a visual of a movie.  User may click a movie cell to bring up a pop-up of a YouTube video.

## Demo
You may see an [example of precomiled website here](http://htmlpreview.github.io/?https://github.com/vaistauga/movieTrailerWebsite/blob/master/fresh_tomatoes.html).

## Usage
### Generate static website which contains a preset list of movies inside python interactive
1. Open Python interactive terminal
1. Import app module
2. run ```showSamplePage()``` method in app module

### Create your own list of movies, then use python to show them in a website
1. Import mediaTypes.py module
3. Create an array of movie objects.  Movie objects can be created by calling mediaTypes.Movie() function. The function takes following paramters:
    1. Title 
    1. Year
    1. Poster URL
    1. Trailer URL - must be Youtube
4. Import fresh_tomatoes.py module
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
* [Starter code](https://github.com/udacity/ud036_StarterCode) supplied by [Udacity](https://github.com/udacity).
* Additional code contributed by [Vaidotas Staugaitis](https://github.com/vaistauga) is offered under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/).
