import pickle                            # file name should not be kept as pickle it won't work
class Employee:
    def __init__(self,name,age):
        self.ename=name
        self.eage=age
    def disp(self):
        print(self.ename)
        print(self.eage)
e1=Employee("shashank",25)
f=open("newfile.txt","wb")
pickle.dump(e1,f)
f.close()
