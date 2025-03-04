class GenerateReport:
    admin_name= "abc"
    admin_password = 1234
    def __init__(self,accno,amount,bal,action):
        self.accno=accno
        self.amount=amount
        self.bal=bal
        self.action=action

    def __str__(self):

        print("Account number = ",self.accno)
        print("Acion = ",self.action)
        print("Amount = ",self.amount)
        print("remaining balance = ",self.bal)

        return"-----------------------------------------------------"