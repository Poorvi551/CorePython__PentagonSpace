l=[10,20,30,40]
print(len(l))
l1=l            #shallow copy
print(l)
print(l1)
l[2]=300
print(l)   # [10, 20, 300, 40]
print(l1)   # [10, 20, 300, 40]