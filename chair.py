class chair:
    def __init__(self):
        self.colour="Blue"
        self.brand="CP"
    def rotate(self):
        self.cost=200
        #cost=500    Local variable
        print(self.cost)
c1=chair()
print(c1.colour)
print(c1.brand)
#print(c1.cost)
c1.rotate()
print(c1.cost)
c1.height=3
print(c1.height)


