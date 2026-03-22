class calci:
    def __init__(self):
        self.num=9
        self.colour="black"
    def add(self):
        a=10
        b=20
        c=a+b
        return c        # With return value
c1=calci()
c1.add()               # No parameter
print(c1.num)
print(c1.colour)
res=c1.add()
print(res)