#HMN=how many number
HMN=int(input("How many numbers would you enter?"))
#num=how many numbers been plused.
num=0
sum=0
while HMN>10 or HMN<=0:
    print("please enter again.")
    HMN = int(input("How many numbers would you enter?"))
while num < HMN:
    num1=int(input("Please enter the number you would like to plus."))
    sum=sum+num1
    num += 1
print(sum)