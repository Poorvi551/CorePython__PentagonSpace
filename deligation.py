class Radio:
    def Turnon(self,x):
        if x==1:
            print("Radio is on")
        else:
            print("Radio is off")
class Car:
    def __init__(self,min,max):
        self.cmin=min
        self.cmax=max
        self.R=Radio()
c1=Car(60,120)
print(c1.cmin)
print(c1.cmax)
c1.R.Turnon(1)
c1.R.Turnon(-2)