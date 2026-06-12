class Plane:
    def takeoff(self):
        print("Plane is taking off")
    def fly(self):
        print("Plane is flying")
class Passenger(Plane):
    pass
class Cargo(Plane):
    pass
class Fighter(Plane):
    pass
p1=Passenger()
c1=Cargo()
f1=Fighter()
def allowplane(ref):
    ref.takeoff()
    ref.fly()
allowplane(p1)
allowplane(c1)
allowplane(f1)


 #or

