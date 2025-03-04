from abc import ABC , abstractmethod
class Account(ABC):
    def __init__(self,account_no,account_holder_name,balance):
        self.account_no=account_no
        self.account_holder_name=account_holder_name
        self.balance=balance

    @abstractmethod
    def deposit(self,amount):
        pass

    @abstractmethod
    def withdrawal(self,amount):
        pass

    @abstractmethod
    def calculate_interest(self,years):
        pass

    def check_balance(self):
        print("current balance: ",self.balance)
        