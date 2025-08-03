class BankAccount:
    def __init__(self,  balance=0):
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return print(f"Deposited:  ${amount}")
        return False
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            #print(f"Withdrew: ${amount}")
            return f"Withdrew: ${amount}" 
        #print("Insufficient funds.") 
        return f"Insufficient funds."
    def get_balance(self):
        return self.balance
    # def __str__(self):
    #     return f"Balance={self.balance})"
    def display_balance(self):
        return f"Current Balance: ${self.balance}"