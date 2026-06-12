a=100
def fun1():
    a=10
    b=20
    print(a)
    print(b)
def fun2():
    a=15
    b=25
    print(a)
    print(b)
print(a)
fun1()
print(a)
fun2()
print(a)

# accessing global variable using global

a=100
def fun1():
    global a
    a=10
    b=20
    print(a)
    print(b)
def fun2():
    a=15
    b=25
    print(a)
    print(b)
print(a)
fun1()
print(a)
fun2()
print(a)
