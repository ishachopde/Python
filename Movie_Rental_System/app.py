import os
import json
from user import User


def Menu():
    #ask for the  user's name
    # check if a file exixts for the entered user
    # if it exists then load the data
    # give a list of option such as:
        # add a movie
        # see list of movies:
            # set the movie as watched
            # delete a movie by name
        # see list of watched movies
        # save and quit

    name = input("Enter user name: ")
    filename = "{}.txt".format(name)
    if file_exists(filename):
        with open(filename, 'r') as file:
            json_data = json.load(file)
        user = User.load_from_json(json_data)
    else:
        user = User(name)

    user_input = input("Enter 'a' to add a movie, 's' to see the list of movies,"
          "'w' to set a movie as watched,'d' to delete a movie,'l' to see a lst of watched movie, 'save' to save data, 'q' to quit")

    while user_input != 'q':

        if user_input == 'a':
            movie_name = input("enter movie name: ")
            movie_genre = input("enter movie genre: ")
            user.add_movie(movie_name,movie_genre)

        elif user_input == 's':
            for movie in user.movies:
                print("Name {} Genre {} Watched {}".format(movie.name,movie.genre,movie.watched))

        elif user_input == 'w':
            set_movie_watched = input(" enter the movie name to  be set as watched: ")
            user.set_watched(set_movie_watched)

        elif user_input == 'd':
            delete_movie = input("enter movie name to be deleted: ")
            user.delete_movie(delete_movie)

        elif user_input == 'l':
            for movie in user.movies_watched():
                print("Name {} Genre {} Watched {}".format(movie.name, movie.genre, movie.watched))

        elif user_input == 'save':
            with open(filename, 'w') as f:
                json.dump(user.json(),f)

        user_input = input("Enter 'a' to add a movie, 's' to see the list of movies,"
                           "'w' to set a movie as watched", "'d' to delete a movie",
                           "'l' to see a lst of watched movie", "'save' to save data", "'q' to quit")

def file_exists(filename):
    return os.path.isfile(filename)

Menu()
