#初始化
eng=[]
up60=[]
up90=[]
s=0
t=0
#输入成绩
for k in range(30):
    eng.append(float(eval(input("请输入学生成绩:"))))
#筛选
for k in range(30):
    if eng[k]>60:
        up60.append(eng[k])
        s=s+1
    if eng[k]>90:
        up90.append(eng[k])
        t=t+1
#输出
print("60分以上的人数为:",s)
print(up60)
print("90分以上的人数为:",t)
print(up90)
