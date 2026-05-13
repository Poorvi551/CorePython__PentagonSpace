class Book:
    def __init__(self,page):
        self.__pages=page    # converting public variable into private variable using ( __ ) double underscore.
b1=Book(100)
print(b1.__pages)