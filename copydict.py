import copy

student={"name":"Sinchu",
         "age":"20",
         "phone":{"mob":200,
                  "land":700},
         "addr":{"resi":"Bangalore",
                 "perm":"Belagavi"}}
print(student)
s1=student.copy()           # Act as shalllow copy
s1["phone"]["mob"]=270
print(s1)
print(student)
s2=copy.deepcopy(student)
s2["addr"]["resi"]="BTM"
print(s2)
print(student)
