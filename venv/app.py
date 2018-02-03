from movie import Movie
from user import User

user = User("Miikka")

my_movie = Movie("The Matrix", "Sci-FI", True)

user.movies.append(my_movie)

# print(user)
print("User movies: {}".format(user.watched_movies()))

