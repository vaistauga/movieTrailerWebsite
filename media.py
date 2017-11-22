import webbrowser

class Movie():
    def __init__(self, movie_title, movie_storyline, movie_image, movie_video):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_image
        self.trailer_youtube_url = movie_video

    def playVideo(self):
        webbrowser.open(self.video)
