import webbrowser


class Media():
    # This class is the parent class of various media type data,
    # only derived classes should be implemented

    def __init__(self, title, short_description, poster_image_url):
        self.title = title
        self.short_description = short_description

        self.poster_image_url = poster_image_url


class Video(Media):
    # this class represents media types who has video as main content,
    # such as Movie or TV Show

    def __init__(self, title, short_description, image, movie_video):
        Media.__init__(self, title, short_description, image)
        self.trailer_youtube_url = movie_video

    def play_video(self):
        # This method opens a browser vindow and loads a web page
        # to the Video trailer_youtube_url variable"""
        webbrowser.open(self.trailer_youtube_url)
