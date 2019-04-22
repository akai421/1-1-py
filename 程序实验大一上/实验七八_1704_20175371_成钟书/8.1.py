
from employees import*

number = int(input("Enter the amount of the employees:"))
aGroup = employees(number)
for i in range(aGroup.number):
    aGroup.setTime(i)
    aGroup.setWage(i)
print("Worker\'s wage:\n",aGroup.getSalary())
