from College import College

obj = College("FC")
ch1=0
while(ch1!=10):
    print('''1. Add Student
             2. display Details
             3. search by name
             4. delete by name
            5. Update by rollno
           10.Exit''')
    ch= int(input("enter choice: "))
    if(ch1 == 1):
        roll = int(input("enter rollno: "))
        name = input("enter name: ")
        marks= int(input("enter marks: "))
        obj.addStudent(roll,name,marks)

    elif(ch == 2):
        obj.display()
    elif(ch == 3):
        roll= int(input("enter rollno to search: "))
        obj.searchByRoll(roll)
    elif(ch == 4):
        nm=input("enter name to ba deleted: ")
    elif(ch == 5):
        roll = int(input("enter rollno to be updated: "))
        obj.updateByRoll(roll)
    else:
        print("byee!!!!!!!!!!!!!!!!!!!!!!!!")
