"""
simple bank account system where we can deposit and check on the balance
"""
# function with a default parameter.
def create_account(balance=0):
    return {"balance": balance}


def deposit(current_account, amount):
    # we want to create a new copy of the existing dict
    return {**current_account, "balance": current_account["balance"] + amount}

def withdraw(current_account, amount):
    if amount>current_account["balance"]:
        print("insufficient funds")
        return current_account
    print(f"{amount} has been withdrawn")
    return {**current_account, "balance": current_account["balance"] - amount}

def get_balance(current_account):
    return current_account["balance"]



#usage
acount1 = create_account()
acount1 = deposit(acount1, 100)
print("balance", get_balance(acount1))
accont1 = withdraw(acount1, 50)
print("balance", get_balance(accont1))



class BankAccount:
    def __init__(self, balance=0):

        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount>self.balance:
            print("insufficient funds")
        else:
            self.balance -= amount

    def get_balance(self):
            return self.balance

    # usage
    account2 = BankAccount()
    account2.deposit(100)
    print(account2.get_balance())
    account2.deposit(1000)
    print(account2.get_balance())
    account2.withdraw(500)
    print(account2.get_balance())
