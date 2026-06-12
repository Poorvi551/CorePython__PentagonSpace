class Car:
    def __init__(self):
        self.brand=""
    def __move(self):
        print("Car is moving")
    def helper(self):
        self.__move()
c1=Car()
c1.helper()