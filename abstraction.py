from abc import ABC,abstractmethod
class Payment(ABC):  # ABC- Abstract Base class
    @abstractmethod
    def Pay(self,Amount):
        pass
class Upi(Payment):
    def Pay(self,Amount):
        if Amount>0:
            print(Amount, "received through UPI")
        else:
            print("Amount, cannot be negative")
class Card(Payment):
    def Pay(self,Amount):
        if Amount > 0:
            print(Amount, "received through Card")
        else:
            print("Amount, cannot be negative")
U=Upi()
C=Card()
U.Pay(100)
C.Pay(200)
U.Pay(-100)
