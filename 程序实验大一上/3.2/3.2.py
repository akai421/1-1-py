while 1:
    rows=eval(input("请输入你想要的列数:"))
    while 1:
        if rows>0:
            break
        print("请输入一个正数")
    if rows%2==0:
        rows=rows-1
    a=(rows+1)/2
    for i in range(int(a)):
        print(" "*(rows-i),"*"*(2*i+1))
