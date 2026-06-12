def generator():
    yield 1
    yield 2
    yield 3
res=generator()           #creating an object generator()
print(res)
print(next(res))
print(next(res))
print(next(res))
#print(next(res))  throws error - Stop iteration error