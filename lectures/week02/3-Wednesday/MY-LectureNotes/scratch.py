#? 8. In this activity, you are going to model a bank account. 

# - Create a class called **BankAccount**. 
# - Add properties for **balance** and **account_number**


# - Allow the user to transfer funds between two accounts. This can be accomplished by adding a **transfer_funds** function to the BankAccount class. 
# - After creating the BankAccount class, along with all the functions make sure to create instance of BankAccount and perform actions. 

# **Example:**


# checking_account = BankAccount("FD332", 100)
# checking_account.deposit(50) 
# print(checking_account.balance) # $150 



class BankAccount:
    
    
    def __init__(self,account_number, balance):
        self.balance = balance
        self.account_number = account_number
        
        
    # - Allow the user to deposit funds to the account. This can be accomplished by adding a **deposit** function to the BankAccount class. 
    def deposit(self, deposit_amount):
        self.balance = self.balance+deposit_amount
        return self.balance
    
    
    # - Allow the user to withdraw funds from the account. This can be accomplished by adding a **withdraw** function to the BankAccount class.
    def withdraw(self, withdraw_amount):
        self.balance = self.balance-withdraw_amount
        return self.balance
    
    def transfer_funds(self, withdraw_from, deposit_to, ammount):
        withdraw_from.balance = withdraw_from.balance - ammount
        deposit_to.balance = deposit_to.balance + ammount
        
    
    
checking_account1 = BankAccount("FD332", 100)
checking_account2 = BankAccount("AB222", 100)

print("Checking account 1 balance: ", checking_account1.balance)
checking_account1.deposit(50)
print("Checking account 1 balance: ", checking_account1.balance)
checking_account1.withdraw(50)
print("Checking account 1 balance: ", checking_account1.balance)

print()
checking_account1.transfer_funds(checking_account1, checking_account2, 50 )
print("Checking account 1 balance: ", checking_account1.balance)
print("Checking account 1 balance: ", checking_account2.balance)