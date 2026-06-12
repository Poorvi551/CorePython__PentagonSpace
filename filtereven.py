def even(num):
    if num%2==0:
        return True
    else:
        return False
l=[]
i=0
while i<=4:
    num=int(input("Enter a num:"))
    l.insert(i,num)
    i=i+1
print(l)
i=0
while i<=4:
    data=l[i]
    choice=even(data)
    if choice==True:
        print(l[i])
    i=i+1