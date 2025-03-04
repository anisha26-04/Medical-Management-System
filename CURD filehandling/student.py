class Student:
  def __init__(self,rollno,name,marks):
      self.__rollno = rollno
      self.__name = name
      self.__marks = marks

  def __str__(self):
      return str(self.__rollno)+" , "+self.__name+" , "+str(self.__marks)+"\n"

  def getRollno(self):
      return self.__rollno
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