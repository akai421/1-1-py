class employees(object):

    def __init__(self,number = 1):
        self._time = [0]*number
        self._wage = [0]*number
        self._salary = [0]*number
        self.number = number

    def setTime(self,index): #设定工时
        if index <= self.number:
                self._time[index-1] = eval(input("Enter the No.%d employee\'s work time(by hour):"%(index)))
                #同时改变总工资
                self._salary[index-1] = self._wage[index-1] * self._time[index-1]
        else:
            print("The employee is not exist.")


    def setWage(self,index): #设定时薪
        if index <= self.number:
                self._wage[index-1] = eval(input("Enter the No.%d employee\'s hourly wage:"%(index)))
                #同时改变总工资
                self._salary[index-1] = self._wage[index-1] * self._time[index-1] 
        else:
            print("The employee is not exist.")

    def getSalary(self):
        return self._salary
