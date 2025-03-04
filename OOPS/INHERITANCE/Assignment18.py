class Student:
    def __init__(self,id,name,age,percentage):
        self.id=id
        self.name=name
        self.age=age
        self.percentage=percentage
    
    def accept(self):
        self.id=int(input("enter student id: "))
        self.name=input("enter student name: ")
        self.age=int(input("enter age of student: "))
        self.percentage=int(input("enter percentage of student: "))

    def display(self):
        print("student ID: ",self.id)
        print("name: ",self.name)
        print("age: ",self.age)
        print("percentage: ",self.percentage)

    def calculateRank(self):
        if self.percentage >= 90 :
            return "A"
        elif self.percentage >= 75 :
            return "B"
        elif self.percentage >= 50 :
            return "C"
        else :
            return "D"
    
class EnggStudent(Student):
    def __init__(self,id,name,age,percentage,branch,internalMarks):
        super().__init__(self,id,name,age,percentage)
        self.branch=branch
        self.internalMarks=internalMarks

    def accept(self):
        super().accept()
        self.branch=input("enter branch: ")
        self.internalMarks=int(input("enter internal marks: "))

    def display(self):
        super().display()
        print("Branch: ",self.branch)
        print("internalMarks: ",self.internalMarks)

    def calculateRank(self):
        total_score=self.percentage + self.internalMarks
        if total_score >= 90 :
            return "A"
        elif total_score >= 75 :
            return "B"
        elif total_score >= 50 :
            return "C"
        else :
            return "D"

         
class MedicalStudent(Student):
    def __init__(self,id,name,age,percentage,specialization,MarksofInternship):
        super().__init__(self,id,name,age,percentage)
        self.specialization=specialization
        self.MarksofInternship=MarksofInternship

    def accept(self):
        super().accept()
        self.specialization=input("enter specialization: ")
        self.MarksofInternship=int(input("enter Marks of Internship: "))

    def display(self):
        super().display()
        print("specialization: ",self.specialization)
        print("internalMarks: ",self.MarksofInternship)

    def calculateRank(self):
        total_score=self.percentage + self.MarksofInternship
        if total_score >= 90 :
            return "A"
        elif total_score >= 75 :
            return "B"
        elif total_score >= 50 :
            return "C"
        else :
            return "D" 
    
class College:
    def _init_(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def remove_student(self, student_id):
        self.students = [student for student in self.students if student.student_id != student_id]

    def _str_(self):
        return "\n".join(str(student) for student in self.students)


# Example execution

college = College()
    
# Adding students
engg_student = EnggStudent("E101", "Alice", 20, 88.5, "Computer Science", 90)
medical_student = MedicalStudent("M102", "Bob", 22, 92.0, "Cardiology", 88)
    
college.add_student(engg_student)
college.add_student(medical_student)
    
# Display all students
print("Students in College:")
print(college)
# Get a student by ID
print("\nDetails of student with ID 'E101':")
student = college.get_student("E101")
if student:
Student.display()
    
# Remove a student
print("\nRemoving student with ID 'M102'")
college.remove_student("M102")
    
# Display all students again
print("\nUpdated Students in College:")
print(college)
    

        
    