class Farmer:
    r=2.5
    def __init__(self,p,t):
        self.principle=p
        self.time=t
    def loan(self):
        si=(self.principle)*(self.time)*(Farmer.r)/100
        print(si)
f1=Farmer(300000,5)
f2=Farmer(500000,7)
f2.loan()
f1.loan()
print(Farmer.r)
