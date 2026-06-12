class Plane:
    def takeoff(self):
        print("Plane is taking off")
    def fly(self):
        print("Plane is Flying")
    def land(self):
        print("Plane is landing")
class Passenger(Plane):
    def carry_p(self):
        print("Plane carries P")
class Cargo(Plane):
    def carry_g(self):
        print("Plane carries G")
class Fighter(Plane):
    def carry_w(self):
        print("Plane carries W")
p1=Passenger()
c1=Cargo()
f1=Fighter()
p1.takeoff()
p1.fly()
p1.land()
p1.carry_p()
c1.takeoff()
c1.fly()
c1.land()
c1.carry_g()
f1.takeoff()
f1.fly()
f1.land()
f1.carry_g()
