from movie import Movie

class User:
    def __init__(self, name):
        self.name = name
        self.movies = []

    def __repr__(self):
        return "User: {}".format(self.name)     # Tehdäänkö tässä palautusarvolla mitään?

    def add_movie(self, name, genre):
        movie = Movie(name, genre, False)
        self.movies.append(movie)

    def delete_movie(self, name):
        # Filtteröidään ja tallennetaan uudellen listaan kaikki objektit, jotka eivät vastaa parametria
        self.movies = list(filter(lambda movie: movie.name != name, self.movies))

    def watched_movies(self):
        # iteroidaan self.movies ja palautetaan ne, joissa watched-muuttuja == watched
        return list(filter(lambda movie: movie.watched, self.movies))

    def json(self):
        return {
            'name': self.name,
            'movies': [ movie.json() for movie in self.movies ]
        }

    # Tätä kutsutaan app.py:ssa:
    # json_data = json.load(f)
    # user = User.from_json(json_data)
    # print(user.json())
    @classmethod
    def from_json(cls, json_data):

        user = User(json_data['name']) # haetaan parametrina annettavasta dictionarysta (json file) nimi
        movies = []
        for movie_data in json_data['movies']:          # luupataan dictionaryn movies-elementti, joka on dictionary
            movies.append(Movie.from_json(movie_data))  # lisätään movies-listaan palautetut elokuvat käyttäen from_json-rakennetta
        user.movies = movies                            # säilötään moviesin sisältö user-objektiin (joka luodaan tämän
                                                        # classmethodin alussa)
        return user                                     # palautetaan user-objekti
