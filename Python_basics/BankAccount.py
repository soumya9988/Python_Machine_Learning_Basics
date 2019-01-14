class BankAccount(object):
    balance = 0

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Account holder %s has %.2f balance' % (self.name, BankAccount.balance)

    def show_balance(self):
        print('Account Holder: ', self.name)
        print('Current balance:', BankAccount.balance)

    def deposit(self, amount):
        if amount <= 0:
            print('Invalid amount!')
            return
        else:
            print('Depositing %.2f $ to your account!'% amount)
            BankAccount.balance += amount
            self.show_balance()

    def withdraw(self, amount):
        if amount <= 0 or amount > BankAccount.balance:
            print('Trying to withdraw %.2f $.. Cannot withdraw that amount' % amount)
            return
        else:
            print('Withdrawing %.2f $ from your account!' % amount)
            BankAccount.balance -= amount
            self.show_balance()


my_account = BankAccount('Nivedh')
print(my_account)
my_account.deposit(10)
my_account.deposit(10000)
my_account.withdraw(20000)
my_account.withdraw(200)



