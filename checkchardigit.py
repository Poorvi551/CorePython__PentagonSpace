str=input("Enter a string:")
print(str)
if str.isalpha():
    print("String contains only alphabet")
elif str.isdigit():
    print("String contains only numbers.")
elif str.isalnum():
    print("String contains both alphabet and numbers")
else:
    print("String contains other characters.")

