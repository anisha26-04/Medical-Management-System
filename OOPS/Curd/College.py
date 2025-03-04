from Student import Students
class College:
    def __init__(self,name):
        self.name=name
        self.listOfStudents= []

    def addStudent(self,rollno,name,marks):
        s=Students(rollno,name,marks)
        self.listOfStudents.append(s)

    def display(self):
        if(len(self.listOfStudents)==0):
            print("no students")
        else:
            for i in self.listOfStudents:
                print (i)

    def searchByRoll(self,roll):
        for i in self.listOfStudents:
            if(i.getRollno() == roll):
                print(i)
                break
            else:
                print("not found")

    def deleteByName(self,nm):
        for i in self.listOfStudents:
            if(i.getName()==nm):
                self.listOfStudents.remove(i)
                print("record deleted")
                break
        else:
            print("not found")

    def updateByRoll(self,roll):
        for i in self.listOfStudents:
            if(i.getRollno()==roll):
                print("1.name")
                print("2.marks")
                ch=int(input("enter chioce: "))
                if(ch==1):
                    nm=input("enter new name: ")
                    i.setName(nm)
                else:
                    m=int(input("enter new marks: "))
                    i.setMarks(m)

                break
        else:
            print("not found")

