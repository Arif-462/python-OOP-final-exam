import random
class User:
    def __init__(self, name) -> None:
        self.name = name        

class Customer(User):
    def __init__(self, name, account_number) -> None:
        super().__init__(name)
        self.account_number = account_number       
        self.Min_withdraw = 100
        self.max_windraw = 500000
        self.transaction_history = []
        self.balance = 0
        self.loan_amount = 0

    def __repr__(self) -> str:
        return f'{self.name},{self.account_number}'
    

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            Banking_management_system.total_balance += amount
            self.transaction_history.append(f'Deposit: {amount}')
            print(f'Deposit: {amount}')

 
    def withdraw(self, amount):
        if amount < self.balance:
            if amount < self.Min_withdraw:
                print(f'Your withdraw amount is very poor you can withdraw more than {self.Min_withdraw}')
            elif amount > self.max_windraw:
                print(f'You can not withdraw over {self.max_windraw}')

            else:
                self.balance -= amount
                Banking_management_system.total_balance -= amount
                self.transaction_history.append(f'withdraw: {amount}')
                print(f'Congratulation! for withdraw {amount} from your {self.account_number}') 
        else:
            print('Your balance is not sufficient')
            print('The bank is bankrupt')  

  
    def get_balance(self):
       print(f'Your available balance is {self.balance}')
       return self.balance


    def transfer_money(self, amount, other_account):
        if amount < self.balance:            
            self.balance -= amount
            other_account += amount
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
            self.transaction_history.append(f'Received loan: {amount}')
            Banking_management_system.total_loan += amount
            Banking_management_system.total_balance -= amount
            print(f'Received {amount} loan to your account')            
        else:
            print(f'You can not receive this {amount} as loan')
            

    def get_loan(self):
        return self.loan_amount



class Banking_management_system:
    def __init__(self):        
        self.accounts = {}
        self.loan_feature = True
    total_balance = 0
    total_loan = 0
        

        
    def create_account(self, name):
        account_number = random.randint(100, 10000)
        for account_number in self.accounts:
            account_number = random.randint(100000, 999999)
        self.accounts[account_number] = self.accounts.get(account_number, name)
        print(f"Account Number: {account_number} created successfully.")
        return account_number
    

    def get_account(self, account_number):
        # return self.accounts.get(account_number, None)
        for account_number, name in self.accounts.items():
            if account_number : name
            return account_number
        
    
    def total_available_balance(self):       
        print(f"Total Available Balance is of the Bank : {self.total_balance}")

    def total_loan_amount(self):             
        print(f"Total Loan is of the Bank : {self.total_loan}")

    def loan_features(self):
        if self.loan_feature is True:
            print("\t\t on")
        else:
            print('\t\t of')





admin = Banking_management_system()

print('\n---------- Created account Holder account----')
act_no_1 = admin.create_account('user1')
user = Customer('abc', act_no_1)

# print(admin.get_account('user'))

print('\n--------------Your diposited money -------------------')
user.deposit(12500)

print('\n\n--------------Your withdrwal money--------------------')
user.withdraw(1000)

print('\n--------------Your Transfer money to another account---')
act_no_2 = admin.create_account('user2')
user.transfer_money(500, act_no_2)

print('\n--------------Your Transaction History-----------------')
user.get_transaction_history()

print('\n--------------Your loan money--------------------------')
user.receive_loan(2000)

print('\n--------------your Current balance---------------------')
user.get_balance()

print('\n--------------Admin can create a account---------------')
admin.create_account('admin')

print('\n--------------Admin check available balance of the bank.')
admin.total_available_balance()

print('\n-------------Loan amount of admin----------------------')
admin.total_loan_amount()

print('\n-------------Loan features of Admin is now ------------')
admin.loan_features()







        

    
        

    

        
