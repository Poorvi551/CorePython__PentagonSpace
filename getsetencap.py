class Person:
    def __init__(self):
        self.__name=""
    def getter(self):
        return self.__name
    def setter(self,name):
        self.__name=name
    getset=property(getter,setter)
p1=Person()
p1.getset="Prathijna"
res=p1.getset
print(res)