import webbrowser

class Media():
    def __init__(self, title, shortDescription, poster_image_url):
        self.title = title
        self.shortDescription = shortDescription
        self.poster_image_url = poster_image_url

class Video(Media):
    def __init__(self, title, shortDescription, image, movie_video):
        Media.__init__(self, title, shortDescription, image)
        self.trailer_youtube_url = movie_video

    def playVideo(self):
        webbrowser.open(self.video)

class Music(Media):
    def __init__(self, title, shortDescription, image, movie_video):
        Media.__init__(self, title, shortDescription, image)
        self.trailer_youtube_url = movie_video

    def playVideo(self):
        webbrowser.open(self.video)
    
class Game(Media):
    def __init__(self, title, shortDescription, image, movie_video):
        Media.__init__(self, title, shortDescription, image)
        self.trailer_youtube_url = movie_video

    def playVideo(self):
        webbrowser.open(self.video)

