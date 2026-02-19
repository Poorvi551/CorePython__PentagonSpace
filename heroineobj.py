class Heroine:
    def __init__(self):
        self.name="Anushka"
        self.age=37
        self.numOfMovies=22
    def act(self):
        print("Anushka is a good actress")
h1=Heroine()
print(h1.name)
print(h1.age)
print(h1.numOfMovies)
h1.act()
#Adding the values
h1.movies="PK"
print(h1.movies)
#modifying the values
h1.age=47
print(h1.age)
#Deleting the value
del h1.numOfMovies
print(h1.numOfMovies)
