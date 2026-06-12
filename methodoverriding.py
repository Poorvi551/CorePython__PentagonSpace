class A:
    def disp(self):
        print("Inside A")
class B(A):
    def disp(self):
        print("Inside B")
class C(B):
    def disp(self):
        print("Inside C")
c1=C()
c1.disp()
c1.disp()
c1.disp()

