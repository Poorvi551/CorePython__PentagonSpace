class Charger:
    def __init__(self):
        self.cname="IQOO Charger"
        print("Charger is ready")
    def getcharger(self):
        print("Charger is plugged")
class Phone:
    def __init__(self):
        self.pname="IQOO"
        self.R=""
        print("Phone is ready")
    def hasphone(self,p):
        self.R=p
p1=Phone()
c1=Charger()
p1.hasphone(c1)
p1.R.getcharger()
del p1
print(c1.cname)
