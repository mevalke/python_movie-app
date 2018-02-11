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

    # Määrittely ilman classmethodia (load from cls file-luvun lopussa):
    # def load_from_file(self, filename):
    #     with open(filename, 'r') as f:  # Avaa parametrina annettu tiedosto
    #         content = f.readlines()     # Lue kaikki tiedoston rivit muutujaan
    #         username = content[0]       # Ensimmäinen rivi sisältää käyttäjänimen
    #         movies = []                 # Luo tyhjä lista, johon lisätään käyttäjän elokuvat
    #         for line in content[1:]:    # iteroidaan tiedoston sisältö 2. rivistä alkaen
    #             movie_data = line.split(",") # pilkotaan rivit listoiksi --> [ 'name', 'genre', 'watched' ]
    #             # Lisätään rivit movies-muuttujaan (watched-elementti listätään vain jos sisältö on True)
    #             movies.append(Movie(movie_data[0], movie_data[1], movie_data[2] == "True"))
    #
    #         user = User(username)       # Tallenna objekti muuttujaan käyttäen User class-rakennetta
    #         user.movies = movies        # Tallenna movies-muuttujan sisältö objektin movies-listaan (User class: self.movies)
    #         return user                 # Palauta user-objekti

    @classmethod
    def load_from_file(cls, filename):  # cls --> class, viittaa User classiin
        with open(filename, 'r') as f:  # Avaa parametrina annettu tiedosto
            content = f.readlines()     # Lue kaikki tiedoston rivit muutujaan
            username = content[0]       # Ensimmäinen rivi sisältää käyttäjänimen
            movies = []                 # Luo tyhjä lista, johon lisätään käyttäjän elokuvat
            for line in content[1:]:    # iteroidaan tiedoston sisältö 2. rivistä alkaen
                movie_data = line.split(",") # pilkotaan rivit listoiksi --> [ 'name', 'genre', 'watched' ]
                # Lisätään rivit movies-muuttujaan (watched-elementti listätään vain jos sisältö on True)
                movies.append(Movie(movie_data[0], movie_data[1], movie_data[2] == "True"))

            user = cls(username)        # HUOM! cls-määrittely! Tallenna objekti muuttujaan käyttäen User class-rakennetta
            user.movies = movies        # Tallenna movies-muuttujan sisältö objektin movies-listaan (User class: self.movies)
            return user                 # Palauta user-objekti
