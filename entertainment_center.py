# -*- coding: utf-8 -*-
"""
Created on Sun May  5 23:13:48 2019

@author: Aishwarya
"""

import movie_website
import media

toy_story = media.Movie("Toy Story","A story of a boy and his toys that come to life","https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg","https://youtu.be/rNk1Wi8SvNc?t=9")  # instance of the class Movie
# here, media is the name of the python file and Movie is the name of the class thats defined inside that media.py file
# when we run this code, then, When we create the instance toy_story, the __init__() function inside the class Movie gets called.
#print(toy_story.storyline)

avatar = media.Movie("Avatar","A marine on alien planet","https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg","https://youtu.be/5PSNL1qE6VY")
#print(avatar.storyline)
#avatar.show_trailer()
school_of_rock = media.Movie("School Of Rock","School of Rock is a 2003 comedy film directed by Richard Linklater,","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSsnbrIouACgszRjtGn_BUCY-oTNrra0Ba06NJd0qJTB1GEGCZUag","https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille","Ratatouille is a 2007 American computer-animated comedy film","https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg","https://www.youtube.com/watch?v=uVeNEbh3A4U")

midnight_in_paris = media.Movie("Midnight In Paris","Midnight in Paris is a 2011 fantasy comedy film","https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg","https://www.youtube.com/watch?v=BYRWfS2s2v4")

harry_potter = media.Movie("Harry Potter","Harry Potter, an eleven-year-old orphan, discovers that he is a wizard and is invited to study at Hogwarts. Even as he escapes a dreary life and enters a world of magic, he finds trouble awaiting him.","https://pbs.twimg.com/profile_images/740298167233585152/Qa7Xs_Gs_400x400.jpg","https://www.youtube.com/watch?v=eKSB0gXl9dw")


movies = [toy_story,avatar,school_of_rock,ratatouille,midnight_in_paris,harry_potter]

movie_website.open_movies_page(movies)



"""
print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)     # The class documentation string.
print(media.Movie.__name__)    # The name of the class.
print(media.Movie.__module__)  # The name of the module in which this class was defined.
print(media.Movie.__bases__)  # The classes from which this class inherits.
print(media.Movie.__dict__)     # The class name space.
"""