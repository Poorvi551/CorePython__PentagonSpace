try:
    a=int(input("Enter a num: "))
    b=int(input("Enter a num: "))
    res=a/b
    print(res)
except ValueError as e:
    print("It is VE")
except ZeroDivisionError as e:
    print("It is ZDE")
except Exception as e:
    print("Error occured")
