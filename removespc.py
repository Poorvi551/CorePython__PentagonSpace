str=" Kiran is drinking " # space is also considered as character in strings
print(str)
res=str.lstrip()
print(res)
res2=str.rstrip()
print(res2)
res3=str.strip()
print(res3)

str=input("Enter a string:")
strng=""
for i in str:
    if i==" ":
        pass
    else:
        strng=strng+i
        print(strng)