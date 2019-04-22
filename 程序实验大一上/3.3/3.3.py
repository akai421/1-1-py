import math
import random


#welcome
print("猜数字游戏")
print("每一次游戏，你都有三次机会去猜盒子里面的数")
print("注:盒子里面的为1-10的数")
#生成随机数
b=0
c=0
while 1:
    e=0 
    a=input("是否开始游戏（是，按y；否，按n）")
    if a=='n' or a=='N':
        break
    elif a=='y' or a=='Y':
        given = math.floor(random.uniform(0,10)) + 1
    b+=1
    given=int(given)
    while e<3:
        e+=1
        guess=eval(input("请输入你猜测的数字:"))
        c+=1
        if guess==given:
            print("恭喜你猜对了")
            break
        elif guess>given:
            print("猜测偏大")
        else :
            print("猜测偏小")
#结束
print("产生了",b,"次随机数")
print("您共猜了",c,"次")
    
    
    
