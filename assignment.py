a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter num for c:"))
if a>b and a>c:
    print("a is greater")
elif b>a and b>c:
    print("b is greater")
elif c>a and c>b:
    print("c is greater")
elif a==b==c:
    print("All the three values are equal ")
else:
    print("Invalid number entry. ")
