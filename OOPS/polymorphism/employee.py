class Employee:
    def __init__(self,id,name,sal):
        self.id=id
        self.name=name
        self.sal=sal

    def display(self):
        print("id=",self.id,"\nname=",self.name,"\nsalary=",self.sal)

    def calculateSal(self):
        return self.sal
    
class HrManager(Employee):
    def __init__(self,id,name,sal,commission):
        super().__init__(id,name,sal)
        self.commission=commission

    def display(self):
        super().display()
        print("commission =",self.commission)

    def calculateSal(self):
        return self.sal + self.commission
    
class Admin(Employee):
    def __init__(self,id,name,sal,allowance):
        super().__init__(id,name,sal)
        self.allowance=allowance

    def display(self):
        super().display()
        print("allowance =",self.allowance)

    def calculateSal(self):
        return self.sal + self.allowance
    
e1=Employee(1,"mansi",10000)
h1=HrManager(2,"anisha",20000,2000)
a1=Admin(3,"pranjali",17000,500)

allemp=[a1,e1,h1]
for i in allemp:
    print("emp info: ")
    i.display()
    print("----------------------------------------------------")
    print("total salary = ",i.calculateSal())
    print("-----------------------------------------------------")
    print("-----------------------------------------------------")


    


