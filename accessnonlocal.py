def outer():
    a=10               # nonlocal variables
    b=20
    print(a)
    print(b)
    def inner():
        # nonlocal a
        a=100       # local variables
        b=200
        print(a)
        print(b)
    print(a)
    inner()
    print(a)   # using nonlocal a prints 100 else 10
outer()