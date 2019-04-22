file = "inputData.txt"
file_object = open(file,'r')                                        #打开文件对象
all_lines = file_object.read().splitlines()                         #把文件中所有行并去掉回车符放入列表中
file_object.close()                                                 #关闭文件

account_of_name = len(all_lines)                                    #获得文件中总人数 
find_name = input("Enter the name you want to find: ")              #用户输入想要查找的姓氏
print("\n")

ans = []                                                            #这是一个答案列表
find_flag = False
#对文件进行遍历的同时找到目标字符串即放入答案列表
for i in range(account_of_name):
    temp = []
    temp = all_lines[i].split()
    print((" ").join(temp))
    del all_lines[i]
    all_lines.insert(i,temp)
    if all_lines[i][1] == find_name:
        find_flag = True
        ans.append((" ").join(temp))

#输出答案
print("\nAccording upper file.")
print("So,anwser is here!\n")
if find_flag:
    for i in ans:
        print(i)
    print("Answer:\tIn total: "+str(len(ans))+" people.\n")
else:
    print("\nAnwser:\tHave no people in this file.\n")

n = input("Enter any key to end!")