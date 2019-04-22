
Employee: empCount=0
def __init__(self, time, salary): 
self.time = time
self.salary = salary
def totalSalary(self): 
return self.salary*self.time
def setTime(self,time): 
self.time=time
def setSalary(self,salary): 
self.salary=salary 
 
Employee.empCount=int(input("How many Employees :"))
emps=np.zeros(Employee.empCount,Employee)
i=0
while(i<Employee.empCount): 
emps[i]=Employee(0,0)
i+=1
i=0 sum=0
while(i<Employee.empCount): 
emps[i].setTime(int(input("NO "+str(i)+" Employee's work time:")))
emps[i].setSalary(int(input("NO "+str(i)+" Employee's work salary:")))
sum = sum + emps[i].totalSalary()
i+=1 
print("Total salary is :"+str(sum))
