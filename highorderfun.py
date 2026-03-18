def fun1():
    print("Inside fun1")
def fun2(ptr):
    print("Entering fun1")
    ptr()
    print("Leaving fun1")
fun1()
fun2(fun1)