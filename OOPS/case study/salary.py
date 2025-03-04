from saving import SavingAccount
from datetime import datetime

class SalaryAccount(SavingAccount):

    interest_rate = 6

    def __init__(self, account_number, holder_name, balance):
        super().__init__(account_number, holder_name, balance)
        self.status = "ACTIVE"
        self.last_transaction_date = datetime.now().date()

    def deposit(self, amount):
        entered_date = input("Enter today's date (DD/MM/YYYY): ")
        if (datetime.strptime(entered_date, "%d/%m/%Y").date() - self.last_transaction_date).days > 60:
            self.status = "FROZEN"
            print("Your account has been frozen. Please activate it to continue.")
        else:
            super().deposit(amount)

    def withdraw(self, amount):
        entered_date = input("Enter today's date (DD/MM/YYYY): ")
        if (datetime.strptime(entered_date, "%d/%m/%Y").date() - self.last_transaction_date).days > 60:
            self.status = "FROZEN"
            print("Your account has been frozen. Please activate it to continue.")
        else:
            super().withdraw(amount)

    def check_interest(self, year):
        super().check_interest(year)

    def show_status(self):
        print("Your account status: " ,self.status)

    def activate_account(self):
        entered_date = input("Enter today's date (DD/MM/YYYY): ")
        print("Do you want to pay Rs. 500 to activate your account? (Y/N)")
        choice = input()

        if choice.lower() == 'y':
            if self.balance > (SavingAccount.minimum_balance + 500):
                self.status = "ACTIVE"
                self.balance -= 500
                self.last_transaction_date = datetime.strptime(entered_date, "%d/%m/%Y").date()
                print("Your account has been activated.")
            else:
                print("Insufficient funds to activate your account.")
                deposit_choice = input("Do you want to deposit money to activate your account? (Y/N): ")
                if deposit_choice.lower() == 'y':
                    deposit_amount = float(input("Enter the amount to deposit: "))
                    self.balance += deposit_amount
                    print(f"Rs. {deposit_amount} deposited. Your account is now activated.")
                else:
                    print("Please activate your account.")
        else:
            print("Account activation canceled.")
