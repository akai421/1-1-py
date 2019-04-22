Number =int(input("Please enter a number:"))
b=Number
if Number >=1:
    print("*".center(b))
for a in range (2,Number+1):
    if a%2 == 1:
        print(("*"*a).center(b))
    elif a%2==0:
        print("")
