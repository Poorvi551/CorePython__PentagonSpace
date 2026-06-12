# ptr=open("filehandling.txt", "r")
# data=ptr.read()
# print(data)
# ptr.close()

# ptr=open("filehandling.txt", "r")
# data=ptr.read(2)
# print(data)
# ptr.close()


# ptr=open("filehandling.txt", "r")
# data=ptr.readline()
# print(data)
# ptr.close()


ptr=open("filehandling.txt", "r")
data=ptr.readlines()
print(data)
ptr.close()