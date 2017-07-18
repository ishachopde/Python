from movie import Movie

class User:
    def __init__(self, name):
        self.name = name
        self.movies = []

    def __repr__(self):
        return "<User {}>".format(self.name)

    def add_movie(self, name, genre):
         movie = Movie(name,genre,False)
         self.movies.append(movie)

    def delete_movie(self, name):
        filter(lambda movie: movie.name != name, self.movies)
        #self.movies.delete(name)

    def movies_watched(self):
        # use filter method
        movies_watched = list(filter(lambda movie: movie.watched, self.movies))
        return movies_watched

    def json(self):
        return {
            "name": self.name,
            "movie": [
                movie.json() for movie in self.movies
            ]
        }

