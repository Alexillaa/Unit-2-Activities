# First, we create the Class BankAccount, in which we define the attributes that each object will have and the order of them.
# In this case, the attribute is balance. We also define a class attribute called bank.
class BankAccount:
    bank = "Central Bank"

    def __init__(self, balance):
        self.balance = balance
# Then we create a method called show_balance, which will print the account's balance. 
    def show_balance(self):
        print(f'Balance: {self.balance}')

# We also create a class method called show_bank, which will print the bank's name. 
    @classmethod
    def show_bank(self):
        print(f'{self.bank}')

# Finally, we create a static method called convert_currency, which will convert dollars to pesos using a fixed exchange rate.
    @staticmethod
    def convert_currency(dollars):
        return dollars * 17.92 

# Finally, we create an instance of the BankAccount class and call the show_balance, show_bank, 
# and convert_currency methods to display the account's balance, bank's name, and converted currency.
# and we print the converted currency to the console.
bankAccount1 = BankAccount(1000) 
bankAccount1.show_balance()
bankAccount1.show_bank()
print(BankAccount.convert_currency(6))
