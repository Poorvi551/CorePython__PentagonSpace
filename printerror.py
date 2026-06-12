try:
    a=int(input("Enter a num: "))
    b=int(input("Enter a num: "))
    res=a/b
    print(res)
except Exception as e:
    print("Error occurred")
    print(e.__str__())
        #or
    print(e)