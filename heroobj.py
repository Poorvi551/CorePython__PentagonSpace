class Hero:
    def __init__(self):
        self.name="Yash"
        self.age=40
        self.numOfMovies=30
    def act(self):
        print("Yash is a good actor.")
h1=Hero()
print(h1.name)
print(h1.age)
print(h1.numOfMovies)
h1.act()