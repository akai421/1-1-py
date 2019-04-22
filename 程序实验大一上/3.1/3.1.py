class_num=eval(input("请输入班级个数:"))
for i in range(class_num):
    class_name=input("请输入班级名:")
    sum=0
    #错误检测
    while 1:
        stu_num=eval(input("请输入学生人数:"))
        if 0<stu_num<=50:
            break
        print("您输入了一个错误数据，请重新输入:")
    for j in range(stu_num):
        ach_num1=eval(input("请输入学生成绩:"))
        sum=sum+ach_num1
    ach_num2=sum/stu_num
    print(class_name,"的平均成绩为",ach_num2)
    
