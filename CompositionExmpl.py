class Os:
    def __init__(self):
        self.status="Active"
        print("Os is installing")
    def getos(self):
        print("Os is still installing")
class Laptop:
    def  __init__(self):
        self.Lname="HP"
        self.O=Os()
        print("Os is installed")
        print("Laptop is ready")
l1=Laptop()
print(l1.Lname)
print(l1.O.status)
l1.O.getos()
print(l1)
print(l1.O)
del l1             #deletes object
l1.O.getos()