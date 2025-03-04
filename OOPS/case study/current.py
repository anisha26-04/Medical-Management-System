from account import Account
class CurrentAccount(Account):
    def _init_(self, account_number, balance, overdraft_limit, overdraft_amount=0, amount_repaid=0):
        super()._init_(account_number, balance, "Current")
        self.overdraft_limit = overdraft_limit
        self.overdraft_amount = overdraft_amount  # Amount already used from overdraft
        self.amount_repaid = amount_repaid  # Amount repaid towards overdraft

    def withdraw(self, amount):
        if amount <= self.balance + (self.overdraft_limit - self.overdraft_amount):
            self.balance -= amount
            self.overdraft_amount += amount
            print("Withdrew", amount, "Current balance:", self.balance, "Overdraft used:", self.overdraft_amount)
        else:
            print("Overdraft limit exceeded")

    def calculate_interest(self):
        print("Interest calculation for current account: No interest applicable")
    
    def check_pending_amount(self):
        pending_amount = self.overdraft_limit - self.overdraft_amount
        print("Pending overdraft amount:", pending_amount)

    def check_status(self):
        if self.overdraft_amount > self.overdraft_limit:
            print("Overdraft limit exceeded!")
        else:
            print("Overdraft is within the limit.")