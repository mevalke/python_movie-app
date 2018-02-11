from user import User

user = User("Miikka")                           # Kutsutaan User-classia ja annetaan parametri, jota käytetään classin
                                                # funktioissa self.name-viittauksilla (esim. save_to_file-funktio)
user.add_movie("The Matrix", "Sci-Fi")          # Movieta ei tarvitse importata, koska se on importattu user.py:ssa,
user.add_movie("The Interview", "Comedy")       # josta leffat lisätään

user.save_to_file()
