str=input("Enter a string:")
rev=""
for i in str:
    rev=i+rev
    print(rev)
if str==rev:
    print("String is a palindrome")
else:
    print("String is not palindrome")
