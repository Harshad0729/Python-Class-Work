class BankAccount:
    def __init__(self, initialAmt, accName):
        self.balance = initialAmt
        self.name = accName
        print("Account created successfully")
        print(f"\n Account for '{self.name}' is created with {self.balance:.2f}")
        
    def getBalance(self):
        print(f"Account created for: {self.name}\n")
        print(f"Opening Balance is: {self.balance}")
        
    def deposite(self, amount):
        self.balance = self.balance + amount
        print("Amount deposite successfully")