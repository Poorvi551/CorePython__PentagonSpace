import pickle                           # File name should not be kept as pickle or unpickle it won't work
class Employee:
    def __init__(self,name,age):
        self.ename=name
        self.eage=age
    def disp(self):
        print(self.ename)
        print(self.eage)
f=open("newfile.txt","rb")
e=pickle.load(f)
e.disp()
f.close()