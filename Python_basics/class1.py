class Customer:
    """
    A customer of ABC Bank with a checking account having attributes:
    name(string) and balance(float)
    """
    @staticmethod
    def print_welcome():
        """
        This is a static method and work without an instance of the class
        """
        print('Welcome to ABC Bank')

    def __init__(self, name, balance = 0.0):
        """
        (string, Float) --> Customer object
        Method that is called when a Customer object is instantiated
        """
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        """
        (float) --> float
        A method that updated the balance of the Customer after withdrawing amount
        """
        if self.balance > amount:
            self.balance -= amount
            return self.balance
        else:
            return 'Not enough fund to withdraw'

    def deposit(self, amount):
        """
        (float) --> float
        Method that accept the amount to be deposited in the customer account 7 returns the new balance of the customer
        """
        self.balance += amount
        return self.balance


Customer.print_welcome()
alex = Customer('Alex', 3000.0)
bal = alex.withdraw(350)
print(bal)
