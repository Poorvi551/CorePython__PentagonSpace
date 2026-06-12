import time
class Demo:
    def printNames(self):
        l=['shashank','rahul','rakshith']
        for i in l:
            print(i)
            time.sleep(3)
    def printNum(self):
        for i in range(10):
            print(i)
            time.sleep(2)
    def add(self):
        a=10
        b=20
        c=a+b
        print(c)
d1=Demo()
d1.printNames()
d1.printNum()
d1.add()