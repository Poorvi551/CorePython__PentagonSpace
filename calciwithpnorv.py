class calci:
    def __init__(self):
        self.num=9
        self.colour="black"
    def add(self,a,b):
        c=a+b
        print(c)      # With return value
c1=calci()
print(c1.num)
print(c1.colour)
x=10
y=20
c1.add(x,y)          # With parameter