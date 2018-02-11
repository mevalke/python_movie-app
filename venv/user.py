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

    def save_to_file(self):             # Kutsutaan app.py:ssa: user.save_to_file()
        # Luodaan tiedosto ja nimetään classille annetun name-parametrin mukaan. Tallennetaan muuttujaan f.
        with open("{}.txt".format(self.name), 'w') as f:
            f.write(self.name + "\n")   # Kirjoitetaan f-muuttujaan (tiedostoon) classin name-parametrin sisältä ja newline
            for movie in self.movies:   # Iteroidaan self.movies-listan sisältö
                # Kirjoitetaan tiedostoon jokaisella iteraatiolla palautettu sisältö ja newline.
                f.write("{},{},{}\n".format(movie.name, movie.genre, str(movie.watched)))

    def load_from_file(self, filename): #
        with open(filename, 'r') as f:
            username = f.readline()