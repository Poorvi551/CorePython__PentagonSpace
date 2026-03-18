def fun1():
    print("Inside fun1.")
def fun2():
    print("Inside fun2")
ptr1=fun1
ptr2=fun2
ptr1()
ptr2()