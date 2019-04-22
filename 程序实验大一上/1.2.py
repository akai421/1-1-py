#1.12
income = eval(input("Please enter the income."))
tax = eval
if income >= 0:
    if income < 50000:
        tax = income*0.005
    elif income <= 100000:
        tax = 2500+(income-50000)*0.007
    else:
        tax = 60000+(income-100000)*0.009
    print("The tax is", tax)
else:
    print("please enter number that is positive")