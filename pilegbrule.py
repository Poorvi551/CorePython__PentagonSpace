from math import pi
#pi=10
def outer():
    #pi=15
    def inner():
        #pi=20
        print(pi)
    inner()
outer()