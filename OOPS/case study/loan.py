from account import Account
class LoanAccount(Account):
    roi=5.3
    def __init__(self,account_no,account_holder_name,balance,loan_amount):
        super().__init__(self,account_no,account_holder_name,balance)
        self.loan_amount=loan_amount

    def deposit(self,amount):
        print("repaying loan amount: ",amount)
        if self.balance >= 0:
            print("loan paid :)")
        else:
            print("remaining amount: ",self.balance)

    def withdrawal(self,amount):
        print("withdrawals not allowed in loan account.")

    def calculate_interest(self,years):
        interest=self.loan_amount * LoanAccount.roi *years /100
        print("interest: ",interest) #display interest

    def update_payment(self,payment):
        if payment > 0:
            self.repaid_amount += payment
            self.loan_amount += payment
            print("you have successfully repaid Rs: ",payment)
            print("your remaining loan balance is Rs: ",-self.loan_amount)
        else:
            print("repaying amount must be positive.")

        
        



                    

        

