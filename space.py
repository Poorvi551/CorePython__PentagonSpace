str=input("Enter a string:")
strng=""  # strings are immutable so the modified string is stored in different variable
for i in str:
    if i==" ":
        pass
    else:
        strng=strng+i
        print(strng)