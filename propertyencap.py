class Person:
    def __init__(self):
        self.__name=""
    @property                          #sets to getter
    def dataAccess(self):
        return self.__name
    @dataAccess.setter                  #sets to setter
    def dataAccess(self,name):
        self.__name = name
p1=Person()
p1.dataAccess="Subbu"
res=p1.dataAccess
print(res)