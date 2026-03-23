class calci:
    def operations(self,a,b):
        c1=a+b
        c2=a-b
        c3=a*b
        c4=a/b
        return c1,c2,c3,c4
c=calci()
res=c.operations(5,2)
print(res)