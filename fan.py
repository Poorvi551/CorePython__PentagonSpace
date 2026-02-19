class Fan:
    def __init__(self):
        self.brand="usha"
        self.colour="brown"
        self.cost=1500
        self.wings=3
    def on(self):
        print("Fan is on")
    def rotate(self):
        print("Fan is rotating")
    def off(self):
        print("Fan is off")
f1=Fan()
print(f1.brand)
print(f1.colour)
print(f1.cost)
print(f1.wings)
f1.on()
f1.rotate()
f1.off()