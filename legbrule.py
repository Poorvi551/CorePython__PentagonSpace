a=10
def outer():
    #a=15
    def inner():
        #a=20
        print(a)
    inner()
outer()