s=set()
for i in range(5):
    data=int(input("Enter a val:"))
    s.add(data)
print(s)
s.update([60,70])
print(s)
s.discard(50)
print(s)
