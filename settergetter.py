class Book:
    def __init__(self,page):
        self.__pages=page    # converting public variable into private variable using ( __ ) double underscore.
    def setter(self,val):
        if val>0:
            self.__pages=val
    def getter(self):
        return self.__pages
b1=Book(100)
res1=b1.getter()
print(res1)
b1.setter(200)
res2=b1.getter()
print(res2)
b1.setter(-99)
res3=b1.getter()
print(res3)