class car:
    def __init__(self):
        self.brand="Kia"
    def dance(self):
        print("Car is dancing")
    @staticmethod
    def drift():
        print("Car is drifting")
    @classmethod
    def move(cls):
        print("Car is moving")
c1=car()
print(c1.brand)
c1.dance()
c1.drift()
c1.move()
car.drift()      # Standard Way - we have standard way to execute so we should use classname.
car.move()       # Standard Way