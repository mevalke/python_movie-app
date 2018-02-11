# Ennnen Load from cls file-lukua
# user = User("Miikka")                           # Kutsutaan User-classia ja annetaan parametri, jota käytetään classin
#                                                 # funktioissa self.name-viittauksilla (esim. save_to_file-funktio)
# user.add_movie("The Matrix", "Sci-Fi")          # Movieta ei tarvitse importata, koska se on importattu user.py:ssa,
# user.add_movie("The Interview", "Comedy")       # josta leffat lisätään

# user.save_to_file()

# Ilman @classmethod-määrittelyä load_from_filessa, sitä kutsuttaisiin näin (muutos load from cls file-luvun lopussa)
# user = User("Miikka")                    # Tämä on tehtävä, että classin sisältämää loaf_from_file-funktiota voidaan
#                                          # kutsua.
# user = user.load_from_file("Miikka.txt") # Suoraan (User.load_from_file) ei voi kutsua, koska funktio on classin sisällä
# print(user.movies)

# user = User.load_from_file("Miikka.txt")
# print(user.name)
# print(user.movies)

from user import User
import json

user = User("Miikka")                       # Tallennus muuttujaan tehtävä, että classin sisältämiä methodeja voidaan
user.add_movie("The Matrix", "Sci-Fi")      # kutsua.
user.add_movie("The Interview", "Comedy")
with open('my_file.txt', 'w') as f:
    json.dump(user.json(), f)               # User clasin sisältämä json-funktio palauttaa dictionaryn, joka tallennetaan
                                            # json-tiedostoon
print(user.movies)

