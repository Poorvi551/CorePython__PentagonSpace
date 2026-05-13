def main():
    print("Inside main")
def outer(ptr):
    print("Inside outer")
    def inner():
        print("Entering inner")
        ptr()
        print("Leaving inner")
    return inner
ref=outer(main)
ref()