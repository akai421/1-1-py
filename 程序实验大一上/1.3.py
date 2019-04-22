Year = int(input("Enter the year:"))
Month = int(input("Enter the month:"))
Day = int(input("Enter the day:"))
HMD = 0
#HMD=how many days
if ((Year % 4 == 0)and(Year % 100 != 0))or(Year % 400 == 0):
    List1 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in range(1, Month):
        HMD += List1[i]
else:
    List2 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in range(1, Month):
        HMD += List2[i]
HMD += Day
print(Year, Month, Day, sep=" ")
print("This is the %dth day of year %d."%(HMD, Year))

