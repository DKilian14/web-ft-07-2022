

# make a deposit to an account. 
menu = ["Print Accounts", "Add Account", "Find Account", "How Much In Bank Vault", "Find Highest Investor", "Make Deposit", "Make Withdrawal", 'Make Transfer', 'Quit' ]

class Bank:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.accounts = []
        
    # add an account holder to the account_holders list    
    def addAccount(self, name, balance):
        accountObj = Account(name, balance)
        self.accounts.append(accountObj)
    # see all of the bank's accounts.  
    
    
    def printAccounts(self):
        for account in self.accounts:
            print(account.name, account.balance)
    # find account information given a name. 
    def findByName(self):
        query = input("Who's account would you like to access? >>")
        exists = False
        for account in self.accounts: 
            if query == account.name: 
                print(f'{account.name} has {account.balance} in their account.')
                return account
        if exists == False:
            print("Not an account. exiting program to prevent system crash. please try again. ") 
            exit()   
            
            
    #find how much the bank is holding. 
    def findBankBalance(self):
        sum = 0 
        for account in self.accounts: 
            sum = sum + account.balance
        print(f"Bank has a total of {sum} in it's coffers")
        
    #find highest account holder. 
    def findHighestInvestor(self):
        account_with_most_money = ''
        highest_amount = 0
        for account in self.accounts:
            if account.balance > highest_amount:
                account_with_most_money = account
                highest_amount = account.balance
        print(f"account with most money = {account_with_most_money.name, account_with_most_money.balance}")
        
    #deposit to an account
    def deposit(self):
        account = self.findByName()
        ammount = int(input("how much to deposit?"))
        account.balance = account.balance+ammount
    #withdraw from an account            
    def withdraw(self):
        account = self.findByName()
        ammount = int(input("how much to withdraw?"))
        account.balance = account.balance-ammount

    #transfer funds from one account to another. 
    def transfer(self):
        print("WITHDRAWING FROM::::", end="")
        withdraw_from = self.findByName()
        
        ammount = int(input("how much to transfer?"))
        
        print("DEPOSITING TO::::", end="")
        deposit_to = self.findByName()
         
        withdraw_from.balance = withdraw_from.balance - ammount
        deposit_to.balance = deposit_to.balance + ammount
        
        
        
class Account:
    def __init__(self, account_name, balance):
        self.name = account_name
        self.balance = balance
        

def showMenu():
    count = 1 
    for i in menu:
        print(f"{count}: {i}")
        count +=1
    return int(input('what would you like to do?'))
    


def engine():
    chase = Bank("Chase", "123 Chase Street")
    
    
    running = True
    while running:
        user_command = showMenu()
        
        if user_command == 1:
            chase.printAccounts()
        elif user_command == 2:
            new_account_name = input('what is the new account user name?  >>')
            new_account_balance = int(input('what is the starting balance?  >>'))
            chase.addAccount(new_account_name, new_account_balance)
        elif user_command == 3:
            chase.findByName()
        elif user_command == 4:
            chase.findBankBalance()
        elif user_command == 5:
            chase.findHighestInvestor()
        elif user_command == 6:
            chase.deposit()
        elif user_command == 7:
            chase.withdraw()
        elif user_command == 8:
            chase.transfer()
        elif user_command == 9:
            print('goodbye')
            exit()



engine()

