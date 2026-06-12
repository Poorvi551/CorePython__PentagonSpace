l=[]
i=0
while i<=4:
    num=int(input("Enter a num:"))
    l.insert(i,num)
    i=i+1
print(l)
res=list(filter(lambda num:num%2==0,l))   # filtering(built-in) using lambda function
print(res)