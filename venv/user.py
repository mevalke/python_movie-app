from movie import Movie

class User:
    def __init__(self, name):                   # Kutsutaan app.py:ssa: user = User("Miikka")
        self.name = name
        self.movies = []

    def __repr__(self):
        return "User: {}".format(self.name)     # Tehdäänkö tässä palautusarvolla mitään?

    def add_movie(self, name, genre):           # Kutsutaan app.py:ssa: user.add_movie("The Matrix", "Sci-Fi")
        movie = Movie(name, genre, False)       # Luodaan objekti lukemalla Movie class-rakenne muuttujaan annetuilla parametreilla
        self.movies.append(movie)               # Lisätään objekti listaan

    def delete_movie(self, name):
        # Filtteröidään ja tallennetaan uudellen listaan kaikki objektit, jotka eivät vastaa parametria
        self.movies = list(filter(lambda movie: movie.name != name, self.movies))

    def watched_movies(self):
        # iteroidaan self.movies ja palautetaan ne, joissa watched-muuttuja == watched
        return list(filter(lambda movie: movie.watched, self.movies))

    def json(self):                             # funktiota kustutaan app.py:ssä: with open('my_file.txt', 'w') as f:
        return {                                #                                       json.dump(user.json(), f)
            'name': self.name,                  # funktio palauttaa: a) nimen (kutsutaan app.py:ssä: user = User("Miikka")
            'movies': [ movie.json() for movie in self.movies ] # b) dictionaryn, joka luodaan iteroimalla self.movies
        }                                                       # jokainen self.moviesin sisältämä list tallennetaan
                                                                # movie.json-rakenteeseen
    @classmethod
    def from_json(cls, json_data):
        user = User(json_data['name'])
        movies = []
        for movie_data in json_data['movies']:
            movies.append(Movie.from_json(movie_data))
        user.movies = movies

        return user
