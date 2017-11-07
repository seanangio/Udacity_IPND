##########################################
# Project 3: Movie Website
# Date Started: 12/6/2016
# Date Completed: 12/6/2016
# Submitted by: Sean Angiolillo
##########################################

# Media File #
# Description: This file creates the class Movie to allow for instances of this
# class to be used in the entertainment.py file. This definition of the class
# Movie was obtained through the course
###############################################################################
import webbrowser


class InvalidRatingException(Exception):
    """class defined in order to raise exception for invalid rating"""
    def __str__(self):
        return "Invalid Movie Rating"


class Movie():
    """This class provides a way to store movie related information"""
    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, rating):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        if(rating not in Movie.VALID_RATINGS):
            raise InvalidRatingException
        self.rating = rating

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
