import pickle
f=open("test.txt","rb")
e=pickle.load(f)
print(e)
f.close()