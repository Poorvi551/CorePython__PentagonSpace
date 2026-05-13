def outer():
    print("Inside outer")

    def inner():
        print("Inside inner")
    return inner
ref=outer()
ref()
