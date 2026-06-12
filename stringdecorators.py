def main():
    str="Hello"
    return str
def outer(ptr):
    print("Inside outer")
    def inner():
        print("Entering inner")
        res=ptr()
        ans=res.upper()
        ans1=res.lower()
        print(ans)
        print(ans1)
        print("Leaving inner")
    return inner
ref=outer(main)
ref()

