#Matthew McKinley what is happening

#sets the bank account for the class, having nohting and no account number
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
#sets the deposit function so you can deposit money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False
#sets the withdraw function so you can take money
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False
#checks how much money you have
    def get_balance(self):
        return self.balance
#you can make an account to hold your money
def create_account():
    account_number = input("Enter account number: ")
    initial_balance = float(input("Enter initial balance: "))
    return BankAccount(account_number, initial_balance)
#sets main so you can run it when you need or to start/restart the code
def main():
    accounts = {}
    while True:
        print("\n1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")
        #sets choice to be what the user inputs
        choice = input("Enter your choice (1-5): ")
        #sets to see if choice is 1, and then if it is then you can make an account
        if choice == '1':
            account = create_account()
            accounts[account.account_number] = account
            print(f"Account {account.account_number} created successfully!")
        #chekcs to see if cohice is 2, 3, or 4, and then if it is then you have to input the account number to get access to your account
        elif choice in ['2', '3', '4']:
            account_number = input("Enter account number: ")
            if account_number in accounts:
                account = accounts[account_number]
                if choice == '2':
                    amount = float(input("Enter deposit amount: "))
                    if account.deposit(amount):
                        print(f"Deposited ${amount:.2f} successfully!")
                    else:
                        print("Invalid deposit amount.")
                #checks to see if cohice is 3, and then it can withdraw money from account
                elif choice == '3':
                    amount = float(input("Enter withdrawal amount: "))
                    if account.withdraw(amount):
                        print(f"Withdrawn ${amount:.2f} successfully!")
                    else:
                        print("Invalid withdrawal amount or insufficient funds.")
                else:
                    print(f"Current balance: ${account.get_balance():.2f}")
            else:
                print("Account not found.")
        #checks to see if cohice is 5, then it leaves.
        elif choice == '5':
            print("Thank you for using our banking system. Goodbye!")
            break
        #if it's not 1-5, it tries again
        else:
            print("Invalid choice. Please try again.")
#runs the function to actually start the code
if __name__ == "__main__":
    main()
    #cohice is better than choice im not fixing typos its my comments my rules hahahahahahahahaahahahahaahahhhahaa iuh a