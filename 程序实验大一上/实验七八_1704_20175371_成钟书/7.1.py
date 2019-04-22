def main():
    choice = 'N'
    print("Program Starts......")
    while choice.upper() == 'N':
        request = input("Enter the surname you want to searching:").title()
        response(request) 
        choice = asking()

def response(surname):
    with open("clients.txt",'r') as names: #这种打开方式不用写file.close()
        count = 0
        print("clients are as follows:")
        for name in names:
            if 65 <= ord(name[0]) and ord(name[0]) <= 90: #判断是否为英文名
                if name.split()[1] == surname:
                    print(name.rstrip())
                    count += 1
            elif name[0] == surname :
                print(name.rstrip(),end = ' ')
                count += 1
        print("\nThe total number of the clients with the surname {0:s} is {1:n}".format(surname,count))

def asking(): #询问是否退出
    answer = input("Would you want to quit the program?Press \"Enter\" for yes,other entry for no:")
    if answer == '':
        print("Quit Program.")
        return 'Y'
    else:
        print("One More Time...")
        return 'N'
    

main()        
    
