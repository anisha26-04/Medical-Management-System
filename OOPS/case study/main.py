from saving import SavingAccount
from salary import SalaryAccount
from current import CurrentAccount
from loan import LoanAccount
from EOD import GenerateReport

def main():
    print("Welcome to the Banking System.")

    while True:
        print("\n--- Main Menu ---")
        print("1. Saving Account")
        print("2. Salary Account ")
        print("3. Current Account ")
        print("4. Loan Account")
        print("5. Generate Report")
        print("6. Exit")
        ch = input("Enter your choice: ")

        if ch == "1":
            print("\n--- Saving Account Menu---")
            acc_no = input("Enter account number: ")
            name = input("enter account holder name: ")
            balance = float(input("enter initial balance: "))
            saving_acc = SavingAccount(acc_no, name, balance)

            while True:
                print("\n1. Deposit")
                print("2. Withdrawal")
                print("3. Calculate Interest")
                print("4. Check Balance")
                print("5. Back to Main Menu")
                sub_choice = input("Enter your choice: ")

                if sub_choice == "1":
                    amount = float(input("Enter amount to deposit: "))
                    saving_acc.deposit(amount)
                elif sub_choice == "2":
                    amount = float(input("Enter amount to withdraw: "))
                    saving_acc.withdrawal(amount)
                elif sub_choice == "3":
                    years = int(input("Enter number of years: "))
                    saving_acc.calculate_interest(years)
                elif sub_choice == "4":
                    saving_acc.check_balance()
                elif sub_choice == "5":
                    break
                else:
                    print("Invalid choice! Try again.")
        
        elif ch == "2":
            print("\n--- Salary Account Menu ---")
            acc_no = input("Enter account number: ")
            holder_name = input("Enter account holder name: ")
            balance = float(input("Enter initial balance: "))
            salary_acc = SalaryAccount(acc_no, holder_name, balance)

            while True:
                print("\n1. Deposit")
                print("2. Withdrawal")
                print("3. Check Balance")
                print("4. Activate Account")
                print("5. Show Status")
                print("6. Back to Main Menu")
                sub_choice = input("Enter your choice: ")

                if sub_choice == "1":
                    amount = float(input("Enter amount to deposit: "))
                    salary_acc.deposit(amount)
                elif sub_choice == "2":
                    amount = float(input("Enter amount to withdraw: "))
                    salary_acc.withdraw(amount)
                elif sub_choice == "3":
                    salary_acc.check_balance()
                elif sub_choice == "4":
                    salary_acc.activate_account()
                elif sub_choice == "5":
                    salary_acc.show_status()
                elif sub_choice == "6":
                    break
                else:
                    print("Invalid choice! Try again.")

        elif ch == "3":
            print("\n--- Current Account Menu ---")
            acc_no = input("Enter account number: ")
            holder_name = input("Enter account holder name: ")
            balance = float(input("Enter initial balance: "))
            overdraft_limit = float(input("Enter overdraft limit: "))
            current_acc = CurrentAccount(acc_no, balance, overdraft_limit)

            while True:
                print("\n1. Withdraw")
                print("2. Check Pending Overdraft Amount")
                print("3. Check Status")
                print("4. Back to Main Menu")
                sub_choice = input("Enter your choice: ")

                if sub_choice == "1":
                    amount = float(input("Enter amount to withdraw: "))
                    current_acc.withdraw(amount)
                elif sub_choice == "2":
                    current_acc.check_pending_amount()
                elif sub_choice == "3":
                    current_acc.check_status()
                elif sub_choice == "4":
                    break
                else:
                    print("Invalid choice! Try again.")

        elif ch == "4":
            print("\n--- Loan Account Menu ---")
            acc_no = input("Enter account number: ")
            holder_name = input("Enter account holder name: ")
            balance = float(input("Enter initial balance: "))
            loan_amount = float(input("Enter loan amount: "))
            loan_acc = LoanAccount(acc_no, holder_name, balance, loan_amount)

            while True:
                print("\n1. Deposit (Repay Loan)")
                print("2. Calculate Interest")
                print("3. Check Balance")
                print("4. Back to Main Menu")
                sub_choice = input("Enter your choice: ")

                if sub_choice == "1":
                    amount = float(input("Enter amount to repay loan: "))
                    loan_acc.deposit(amount)
                elif sub_choice == "2":
                    years = int(input("Enter number of years: "))
                    loan_acc.calculate_interest(years)
                elif sub_choice == "3":
                    loan_acc.check_balance()
                elif sub_choice == "4":
                    break
                else:
                    print("Invalid choice! Try again.")

        elif ch == "5":
            print("\n--- Generate Report ---")
            acc_no = input("Enter account number: ")
            action = input("Enter action (e.g., Deposit, Withdrawal): ")
            amount = float(input("Enter transaction amount: "))
            balance = float(input("Enter remaining balance: "))
            report = GenerateReport(acc_no, amount, balance, action)
            print(report)

        elif ch == "6":
            print("Exiting the Banking System. Thank you!")
            break

        else:
            print("Invalid choice! Try again.")
if __name__ == "_main_":
    main()



