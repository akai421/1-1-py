ST=input("please enter a string")
num=0
letter=0
space=0
other=0
for i in ST:
    if ord(i)==32:
        space+=1
    elif ord(i)>=48 and ord(i)<=57:
        num+=1
    elif (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122):
        letter+=1
    else:
        other+=1
print("The number of spaces,numbers,letters and other is",space,num,letter,other)