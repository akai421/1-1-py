#This program is used to calculate tax
Taxableincome=int(input("Enter the Taxableincome:"))
#Get the user’s Taxable income
if(Taxableincome<0)
   Print("You can not input a negative number")
#Prevent the user from inputing a negative number mistakenly 
     if(Taxableincome>=0)and(Taxableincome<=50000)
        Tax Rate=0.05
        Tax= Taxableincome* Tax Rate
#Calculate the tax
       else
        if  (Taxableincome>50000)AND(Taxableincome<=100000)
          Tax Rate=0.07
          Tax=2500+( Taxableincome-50000)* Tax Rate
         else
             Tax Rate=0.09
             Tax=6000+( Taxableincome-100000)* Tax Rate
             Print(“Tax”)
