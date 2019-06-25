# -*- coding: utf-8 -*-
"""
Created on Sun May  5 23:12:47 2019

@author: Aishwarya
"""

import webbrowser
# class definition
class Movie:
    """This class provides a way to store movie related information"""
    # class variables
    VALID_RATINGS = ["G","PG","PG-13","R"]      # for constants, Google Python style recommends capital letters
    
    
    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube):
        # initializing the pieces ofinformation we want to remember
        # instance variables
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
        
        
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)