class A:
    def disp(self):
        print("Inside A")
class B:
    def disp(self):
        print("Inside B")
class C:
    def disp(self):
        print("Inside C")
        B.disp(self)
        A.disp(self)
c1=C()
c1.disp()