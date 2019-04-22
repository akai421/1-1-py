classnumber=int(input("Please enter the number of classes :"))
for i  in range (classnumber):
  studentnumber = int(input("Please enter the number of the students:"))
  while studentnumber>50:
        print("Wrong")         
        studentnumber = int(input("Please enter a new number:"))        
Name = []
Score = []
count = 0
print("Please enter a student'name:(input '*' to end)")
TempName = input()
if TempName !="*": 
      print("Please enter this student's score:")
      TempScore = float(input())
      Name.append(TempName)
      Score.append(TempScore)
      count+=1
      print("Enter the next student' name:(input '*' to end)")
      TempName = input()
      if TempName !="*":
        print("Enter this student'score:")
        TempScore = float(input())
K = 0
while K<count:
   print(Name[K],Score[K])
   K+=1
