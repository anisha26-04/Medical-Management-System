import os
from student import Student
class College:
    def addStudent(self):
        rollno = int(input("enter rollno: "))
        name = input("enter name: ")
        marks = int(input("enter marks: "))
        s= Student(rollno,name,marks)
        f1=open("data.text","a")#here we are going to open the file and append the data
        f1.write(str(s))
        f1.close()

    def display(self):
        if(os.path.exists("data.txt")):

            with open("data.txt","r") as f1:
                for x in f1:
                    sep_text= x.split(",") # split returns list
                    print("roll no: "+sep_text[0])
                    print("name: "+sep_text[1])
                    print("marks: "+sep_text[2])

        else:
            print("file not found")

    def search(self,rollno):
        with open("data.txt","r") as fp:
            for x in fp:
                sep_text = x.split(",")
                if(str(rollno)== sep_text[0]):
                    print("roll no: "+sep_text[0])
                    print("Name: "+sep_text[1])
                    print("marks: "+sep_text[2])
                    break
            else:
                print("Student not found")

    def delete(self,rollno):
        container = []
        isfound = False  #it is used to see if values are added to list
        #open file for reading
        with open("data.txt","r") as fp:
            #read one line
            for x in fp:
                #split text
                sep_text = x.split(",")
                # add non matching records to the container
                if(str(rollno)!= sep_text[0]):
                    container.append(x)
                else:
                    isfound=True

            #if roll number not present
            if (isfound == False):
                print("not found")


            #execute if rollno found
            else:
                #open file in w mode
                with open("data.txt","w") as fp:
                    #write data from container to file line by line
                    for x in container:
                        fp.write(x) 
    def update(self,rollno):
            container = []
            isfound =False
            with open("data.txt","r") as fp :
                #read one line
                for x in fp:
                    sep_text= x.split(",")
                    if(str(rollno)== sep_text[0]):
                        isfound=True
                        # take input from user
                        print("1.name\n2. Marks")
                        ch= int(input("enter choice: "))
                        if(ch==1):
                            nm=input("enter new name: ")
                            sep_text[1]=nm
                        else:
                            m = input("enter marks: ")
                            sep_text[2]= m+"\n"

                        # convert list to string
                        x= ",".join(sep_text)
                        #add to container
                        container.append(x)
                    else:
                        container.append(x)

            if(isfound==True):
                with open("data.txt","w")as fp:
                    for x in container:
                        fp.write(x)
            else:
                print("student not found")

            

