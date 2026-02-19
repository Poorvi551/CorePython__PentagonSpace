class Person:
    def __init__(self):
        self.name="Rahul"
        self.age=29
        self.sal=150000
        self.gf=7
    def sing(self):
        print("Rahul is a romantic singer")
        print(self.name)
        print(self)
p1=Person()
print(p1.name)
print(p1.age)
print(p1.sal)
print(p1.gf)
p1.sing()
print(p1)