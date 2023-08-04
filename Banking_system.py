import random
class User:
    def __init__(self, name) -> None:
        self.name = name        

class Customer(User):
    def __init__(self, name, account_number) -> None:
        super().__init__(name)
        self.account_number = account_number       
        self.balance = 0
        self.Min_withdraw = 100
        self.max_windraw = 500000
        self.transaction_history = []
        self.loan_amount = 0

    def __repr__(self) -> str:
        return f'{self.name},{self.account_number}'
    

    def deposite(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f'Deposite: {amount}')
            print(f'Deposite: {amount}')

 
    def withdraw(self, amount):
        if amount < self.balance:
            if amount < self.Min_withdraw:
                print(f'Your withdraw amount is very poor you can withdraw more than {self.Min_withdraw}')
            elif amount > self.max_windraw:
                print(f'You can not withdraw over {self.max_windraw}')

            else:
                self.balance -= amount
                self.transaction_history.append(f'withdraw: {amount}')
                print(f'Congratulation! for withdraw {amount} from your {self.account_number}') 
        else:
            print('Your balance is not sufficient')
            print('The bank is bankrupt')   

    def get_balance(self):
       print(f'Your available balance is {self.balance}')


    def transfer_money(self, amount, other_account):
        if amount < self.balance:            
            self.balance -= amount
            self.transaction_history.append(f'Transfer {amount} to account No: {other_account}')
            print(f'{amount} transfered from your account to {other_account}')
        else:
            print(f'Your have no enough money to transfer')
            print('The bank is bankrupt.')    

    def get_transaction_history(self):
        print(f'Transaction history for {self.account_number}:')
        for trans in self.transaction_history:
            print(trans)

    
    def receive_loan(self, amount):
        if amount <= self.balance*2:
            self.balance += amount
            self.loan_amount += amount
            print(f'Received {amount} loan to your account')
            return amount
        else:
            print(f'You can not receive this {amount} as loan')


class Banking_management_system:
    def __init__(self):        
        self.accounts = {}
        self.total_balance = 0
        self.total_loan = 0
        self.loan_feature = True

    def create_account(self, name):
        account_number = random.randint(100, 10000)
        while account_number in self.accounts:
            account_number = random.randint(100, 10000)
        self.accounts[account_number] = Customer(name, account_number)
        print(f"Account Number: {account_number} created successfully.")
        return account_number
    
    
    def total_available_balance(self):          
        for account in self.accounts.values():
            self.total_balance += account.balance  
        print(f"Total Available Balance is: {self.total_balance}")

    def total_loan_amount(self):
        for account in self.accounts.values():
            self.total_loan += account.balance*2       
        print(f"Total Loan is: {self.total_loan}")

    def loan_features(self):
        if self.loan_feature is True:
            print("   off  ")
        else:
            print('   on   ')





admin = Banking_management_system()

user = Customer('abc', admin.create_account('user'))

print('=========Your diposited money==========================')
user.deposite(12500)

print('=========Your withdrwal money==========================')
user.withdraw(500000)

print('=========Your Transfer money to another account========')
user.transfer_money(500, admin.create_account('other user'))

print('=========Your Transaction History======================')
user.get_transaction_history()

print('=========Your loan money===============================')
user.receive_loan(2000)

print('=========your balance==================================')
user.get_balance()

print('========Admin can create a account=====================')
admin.create_account('admin')

print('========Admin check avialble balance===================')
admin.total_available_balance()

print('========Loan amount of admin========================== ')
admin.total_loan_amount()

print('========Loan features of Admin is now================= ')
admin.loan_features()








        

    
        

    

        