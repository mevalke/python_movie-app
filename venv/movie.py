class Movie:
    def __init__(self, name, genre, watched):
        self.name = name
        self.genre = genre
        self.watched = watched

    def __repr__(self):
        return "{}".format(self.name)

    def json(self):
        return {
            'name': self.name,
            'genre': self.genre,
            'watched': self.watched
        }
    # Tätä kutsutaan user.pyssa:
    # for movie_data in json_data['movies']:
    # 		movies.append(Movie.from_json(movie_data))
    @classmethod
    def from_json(cls, json_data):          # Tämä palauttaa sille for luupin iteraatiolla syötetyn elokuvan
        return Movie(json_data['name'], json_data['genre'], json_data['watched'])
        # Ylläoleva palautusarvo käyttäen argument unpackingiä:
        # return Movie(**json_data)


