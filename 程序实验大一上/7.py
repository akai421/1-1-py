nameCount=int(input("How many names to store :"))
i=0
while (i<nameCount):
    with open('names.csv', 'a') as nameFile:
Writer= csv.
writer(nameFile)：
firstName = input("Enter name["+str(i)+"]'s firstName :")
lastName = input("Enter name["+str(i)+"]'s lastName :")
Writer.writerow([firstName,lastName])
nameFile.close()
i+=1 
csv_reader = csv.reader(open('names.csv', encoding='utf-8'))
name=input("Enter the lastName you want :")
for row in csv_reader:
    if row[1]==name: 
        print(row) 

