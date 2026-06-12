import pickle
l=[1,2,3,4,5]
f=open("test.txt","wb")
pickle.dump(l,f)
f.close()
f=open("test.txt","rb")
e=pickle.load(f)
print(e)
f.close()
