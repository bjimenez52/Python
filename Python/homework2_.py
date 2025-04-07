'''
Homework2
Name: Bianca Jimenez
github link: https://github.com/bjimenez52/Python/tree/main/Python
Note: Remember to use comments for each function.
doc strings should include what each input consists of, 
what the expected output is and a description of the function.
'''

class Bank_Account: # Bank Account Class
    def __init__(self,name,starting_amount): # Constructor
        self.name=name # Account Holder Name
        self.account = starting_amount # Account Balance
    
    def __repr__(self): # Representation of the object
        return f"Bank_Account(name='{self.name}', Account Balance={self.account})" # Account Balance
    
    def __str__(self): # String representation of the object
        return f"Account Name: {self.name}\nAccount Balance: {self.account}" # Account Balance
    
    def deposit(self,amount): # Deposit method
        if amount>0: # Check if it is positive
            self.account += amount # Add amount to account balance
            print(f"{amount} deposited. New balance: {self.account}") # Print new balance
        else: # Check if it is negative
            print(f"Please deposit a positive number.") # Print error message
    
    def withdraw(self,amount): # Withdraw method
        if amount>0: # Check if it is positive
            if self.account-amount>=0: # Check if the account has sufficient funds
                self.account-=amount # Deduct amount from account balance
                print(f"{amount} withdrawn. New balance: {self.account}") # Print new balance
            else: # Check if the account has insufficient funds
                print(f"Insufficient funds.") # Print error message
        else: # Check if it is negative
            print(f"Please withdraw an amount greater than zero.") # Print error message
    
    def check_balance(self): # Check Balance method
        """
        Check and return the balance of the account holder's account.
        """
        print(f"Balance: {self.account}") # Print account balance

class SavingsAccount(Bank_Account): # Savings Account Class
    def __init__(self,name,starting_amount,interest_rate=1.0): # Constructor
        super().__init__(name,starting_amount) # Call parent constructor
        self.interest_rate=interest_rate # Interest Rate
    
    def __repr__(self): # Representation of the object
        return f"SavingsAccount(account_holder='{self.name}', balance={self.account}, interest_rate={self.interest_rate}%)" # Account Balance
    
    def __str__(self): # String representation of the object
        return f"Savings Account - {self.name}: Balance = ${self.account:.2f}, Interest Rate = {self.interest_rate}%" # Account Balance
    
    def apply_interest(self): # Apply Interest method
        self.account += self.account * (self.interest_rate / 100) # Calculate interest
        return self.account # Return new balance

class CheckingAccount(Bank_Account): # Checking Account Class
    def __init__(self,name,starting_amount,overdraft_limit=100.0): # Constructor
        super().__init__(name,starting_amount) # Call parent constructor
        self.overdraft_limit=overdraft_limit # Overdraft Limit
    
    def __repr__(self): # Representation of the object
        return f"CheckingAccount(account_holder='{self.name}', balance={self.account}, overdraft_limit={self.overdraft_limit})" # Account Balance
    
    def __str__(self): # String representation of the object
        return f"Checking Account - {self.name}: Balance = ${self.account:.2f}, Overdraft Limit = ${self.overdraft_limit:.2f}" # Account Balance
    def withdraw(self,amount): # Withdraw method
        if amount>0: # Check if it is positive
            if self.account-amount>=-self.overdraft_limit: # Check if the account has sufficient funds
                self.account-=amount # Deduct amount from account balance
                print(f"{self.account}") # Print new balance
            else: # Check if the account has insufficient funds
                print(f"Withdrawal exceeds overdraft limit.") # Print error message
        else: # Check if it is negative
            print(f"Withdrawal amount must be positive.") # Print error message

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest2.py'))