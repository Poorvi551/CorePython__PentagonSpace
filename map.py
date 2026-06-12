l=[]
i=0
while i<=4:
    num=int(input("Enter a num:"))
    l.insert(i,num)
    i=i+1
print(l)
def add(num):
    return num+10
res=list(map(add,l))    # Mapping - built-in function
print(res)

# using lambda function
res1=list(map(lambda num:num+10,l))
print(res1)