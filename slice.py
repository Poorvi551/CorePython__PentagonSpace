str="RajaRamMohanRoy"
print(str)  #RajaRamMohanRoy
print(len(str))   #15
print(str[2:6])   #jaRa
print(str[2:7:2])  #jRm
print(str[-2:-8])  # no output --> end value
print(str[-5:-13:-1])   #ahoMmaRa
print(str[10:5])        #no output --> end value
print(str[-11:10])     #RamMoh
print(str[-9:-4])     #mMoha
print(str[-2:-8:-3])  #oa
print(str[6:13:-1])   #no output --> end value
print(str[12:-14:-1])  #RnahoMmaRaj
print(str[::2])        #RjRmoaRy
#print(str[2:8:0])      #error --> step value cannot be 0
print(str[::-1])        #yoRnahoMmaRajaR
print(str[::])          #RajaRamMohanRoy
