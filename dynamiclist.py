L=[]
i=0
while True:
    num=int(input("Enter a num:"))
    L.insert(i,num)
    i+=1
    print("Do you want to continue")
    print("Press 1 yes")
    print("Press 2 No")
    choice=int(input())
    if choice==1:
        continue
    else:
        break
print(L)