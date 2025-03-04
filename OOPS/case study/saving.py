from account import Account
class SavingAccount(Account):
    mini_balance=10000
    rate_of_intrest=0.2
    def __init__(self,account_no,account_holder_name,balance):
        super().__init__(self,account_no,account_holder_name,balance)
        

    def deposit(self,amount):
        self.balance += amount
        print("deposited: Rs ",amount,"new balance: ",self.balance)

    def withdrawal(self,amount):
        if ((self.balance-amount )> SavingAccount.mini_balance):
            self.balance -= amount
            print("withdraw amount: Rs",amount,"new balance: ",self.balance)
        else:
            ("cannot withdraw amount as you have less balance.")

    def calculate_interest(self, years):
        current_balance= self.balance #here we store original balance
        for i in range(years):
            updated_balance=(current_balance * SavingAccount.rate_of_intrest)/100
            current_balance=updated_balance
            print("interest: ",current_balance - self.balance)

    
    def check_balance(self):
        super().check_balance(self)
        

        

        

