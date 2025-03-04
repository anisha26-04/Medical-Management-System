from college import College
if(__name__ =="__main__"):
    ch =0
    obj = College()
    while(ch!=6):
        print('''1. Add student
            2. Display
            3. Search
            4. Delete
            5. Update
            6. Exit''')
        ch = int(input("Enter choice: "))
        if(ch==1):
            obj.addStudent()
        elif(ch== 2):
           obj.display()
        elif(ch==3):
            rollno = int(input("Enter rollno to search: "))
            obj.search(rollno)
        elif(ch==4):
            rollno = int(input("Enter rollno to delete: "))
            obj.delete(rollno)

        elif(ch==5):
            rollno = int(input("enter roll no to update: "))
            obj.update(rollno)