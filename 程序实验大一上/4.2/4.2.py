#输入
String1=str(input("请输入字符串1："))
String2=str(input("请输入字符串2："))
String3=""
#根据用户需要，进行操作
while 1: 
    print("比较，按1；追加，按2；拷贝，按3；结束，按0")
    K=int((input()))
    if K==0:
        break
    elif K==1:
        if String1>String2:
                  print("String 1>String 2")
        elif String1==String2:
                  print("String 1=String 2")
        elif String1<String2:
                  print("String 1<String 2")
    elif K==2:
        String3=String1+String2
        print("结果为:"+String3)
    elif K==3:
        String1=String2
        print("字符串1为"+String1)
