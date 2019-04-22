EnglishScore=[]
TempName=[]
sixtyplus=0
ninetyplus=0
for count in range(30):
    TempName.append(input("Please enter a student's name:\n"))
    TempScore=float(input("Please enter a score:\n"))
    TempName.append(TempScore)
    EnglishScore.append(TempName)
    TempName=[]
    if TempScore >60:
        sixtyplus+=1
        if TempScore>90:
            ninetyplus+=1
print(EnglishScore)
print("The number of students who get 60+ is:",sixtyplus)
print("The number of students who get 90+ is:",ninetyplus)
