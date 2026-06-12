emp_id=[101,102,103,104]
names=["Shaky","Rahul","Rakshith","Nehru"]
res=dict(zip(emp_id,names))
print(res)
mob=[11,420,840,7]
addr=["Pak","Afghan","Thai","India"]
#info=dict(zip(emp_id,names,mob,addr))
#print(info)   #Error
res1=list(zip(names,mob,addr))
final_info=dict(zip(emp_id,res1))
print(final_info)