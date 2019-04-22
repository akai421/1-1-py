Month = 2
a = 1
b = 1
c = 0
while Month < 20:
    Month += 1
    c = a+b
    a = b
    b = c
    print("The amount of the rabbit in month", Month, "is", c)
input()