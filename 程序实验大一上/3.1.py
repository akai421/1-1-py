# -*- coding:utf-8 -*-
sum=0
classnum=0
studentnum=0 
classnumber=int(input("Input the amount of Classes:"))
while(classnum<classnumber):
 if classnum==classnumber: 
  break
 else: 
   studentnumber = int(input("Input the amount of Students:"))
while(studentnum<studentnumber):
      if studentnum==studentnumber: 
         break
      else: 
           score = int(input("Input student's score:"))
           sum=sum+score; studentnum+=1;
           print("Total score is "+str(sum))
classnum+=1;
sum=0
studentnum=0
 
      
