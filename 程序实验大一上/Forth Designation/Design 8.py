class employees:
    def __init__(self, time=8,hoursalary=2):
        self._time = time
        self._hoursalary = hoursalary
        self._salary = time*hoursalary

    def set_time(self,time):
        self._time = time
    def set_hoursalary(self,hoursalary):
        self._hoursalary = hoursalary

    def get_time(self):
        return self._time
    def get_hoursalary(self):
        return self._hoursalary
    def get_salary(self):
        return self._salary

    def __str__(self):
        return str(self._time)+str(self._hoursalary)+str(self._salary)

Myemployees = []
totol = 0
number_of_employees = int(input("Enter the number of employees: "))
for i in range(number_of_employees):
    time = eval(input("Enter the {0:d}th employee's worktime :".format(i+1)))
    hoursalary = eval(input("Enter the {0:d}th employee's salary per hour: ".format(i+1)))
    em = employees(time,hoursalary)
    Myemployees.append(em)
    totol += em.get_salary()

dialog = 0
average = totol/number_of_employees
for i in range(number_of_employees):
    if Myemployees[i].get_salary() > average:
        dialog += 1

print("Total ${0:,d}   Average ${1:.2f}   Diaglog {2:d}".format(totol,average,dialog))

