def outer():
    a=10     # non local variable
    b=20
    print(a)
    print(b)
    def inner():
        c=500    # local variable
        d=700
        print(c)
        print(d)
    inner()
outer()

