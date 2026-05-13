class Brain:
    def __init__(self):
        self.status="Active"
        print("Brain is Active")
    def getbrain(self):
        print("Brain is not working")

class Car:
    def __init__(self):
        self.cname="Maruthi 800"
        print("car is ready")
    def getcar(self):
        print("I love my car")

class Person:
    def __init__(self):
        self.pname="Yash"
        self.B=Brain()
        self.P=""
        print("Yash is a hero")
    def hasperson(self,R):
        self.P=R

p1=Person()
c1=Car()
p1.hasperson(c1)
p1.B.getbrain()
p1.P.getcar()
del p1
c1.getcar()
#p1.B.getbrain()   Error
