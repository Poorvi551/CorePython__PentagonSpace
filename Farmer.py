class Farmer:
    def __init__(self,p,t,r):
        self.principle=p
        self.time=t
        self.rate=r
    def loan(self):
        si=(self.principle)*(self.time)*(self.rate)/100
        print(si)
f1=Farmer(300000,5,2.5)
f2=Farmer(500000,7,2.5)
f2.loan()
f1.loan()