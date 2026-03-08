str="Ahlya is playing"
str1=str.split()
print(str)                      # Ahlya is playing
print(str1)                     # after splitting words are stored as list values['Ahlya','is','playing']
rev=""
for i in str1:
    #rev=i+rev                   Space will not be printed  //playingisAhlya
    rev=i+" "+rev                # Space will be printed    // plaing is Ahlya
    print(rev)
