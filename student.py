class Student:
    def __init__(self):
        self.name="Poorvi"
        self.age=21
        self.usn="4SH22IS050"
    def study(self):
        print("Poorvi is studying")
    def walk(self):
        print("Poorvi is walking")
    def sleep(self):
        print("Poorvi is sleeping")
    def eat(self):
        print("Poorvi is eating")
s1=Student()
print(s1.name)
print(s1.age)
print(s1.usn)
s1.study()
s1.walk()
s1.sleep()
s1.eat()