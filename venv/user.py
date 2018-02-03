from movie import Movie

class User:
    def __init__(self, name):
        self.name = name
        self.movies = []

    def __repr__(self):
        return "User: {}".format(self.name)

    def add_movie(self, name, genre):
        movie = Movie(name, genre, False)
        self.movies.append(movie)

    def delete_movie(self, name):
        self.movies = list(filter(lambda movie: movie.name != name, self.movies))

    def watched_movies(self):
        # watched_movies_list = []
        #
        # for movie in self.movies:
        #     if movie.watched == True:
        #         watched_movies_list.append(movie)
        #
        # return watched_movies_list
        return list(filter(lambda movie: movie.watched, self.movies))