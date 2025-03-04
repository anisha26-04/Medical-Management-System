
class Student:
    def __init__(self,rollno, name, marks):
        self.__rollno = rollno
        self.__name = name
        self.__marks = marks
    
    def __str__(self):
        s = "   Rollno:" + str(self.__rollno)
        s += "  Name: "+self.__name
        s += "  Marks: "+str(self.__marks)
        return s
    
    #getter/ accessor
    def getRollno(self):
        return self.__rollno
    #setter/mutator
    def setRollno(self,roll):
        self.__rollno = roll

    def getName(self):
        return self.__name
    def setName(self,nm):
        self.__name = nm

    def getMarks(self):
        return self.__marks
    def setMarks(self,m):
        self.__marks = m