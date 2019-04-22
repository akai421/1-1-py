n=eval(input("请输入A,B两个矩阵的行数:"))
names=locals()
for i in range(n):
    names['A%s'%i]=[]
    for k in range(n):
        names['A%s'%i].append(eval(input("请输入A:")))
for i in range(n):
    names['B%s'%i]=[]
    for k in range(n):
        names['B%s'%i].append(eval(input("请输入B:")))
for k in range(n):
    names['b%s'%k]=[]
    for j in range(n):
        names['b%s'%k].append(names['B%s'%j][k])
for i in range(n):
    names['C%s'%i]=[]
    sum=0
    for j in range(n):
        for k in range(n):
            sum=(names['A%s'%i][k])*(names['b%s'%j][k])
        names['C%s'%i].append(sum)
for i in range(n):
    print("结果为:",names['C%s'%i])
