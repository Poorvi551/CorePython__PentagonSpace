l=[10,20,30,40]
print(len(l))
l1=l.copy()            #deep copy
print(l)
print(l1)
l[1]=200
print(l)   # [10, 200, 30, 40]
print(l1)   # [10, 20, 30, 40]