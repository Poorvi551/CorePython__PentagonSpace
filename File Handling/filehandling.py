# name=input("Enter a name:")
# ptr=open("filehandling.txt","w")
# ptr.write(name)
# ptr.close()

name=input("Enter a name:")
ptr=open("filehandling.txt","a")
ptr.write(name+"\n")
ptr.close()
