'''
Homework1
Name: Bianca Jimenez
github link: https://github.com/bjimenez52/Python/tree/main/Python
Note: Remember to use comments for each function.
doc strings should include what each input consists of, 
what the expected output is and a description of the function.
'''

class Bank_Account: # Class to represent a bank account
    def __init__(self,name,starting_amount):  # Constructor method
        self.name = name # Initialize the account holder's name
        self.account = starting_amount # Initialize the account balance
    
    def __repr__(self): # Representation method for the class
        return f"Bank_Account(name='{self.name}', Account Balance={self.account})" # String representation of the object
    
    def __str__(self): # String method for the class
        return f"Account Name: {self.name}\nAccount Balance: {self.account}" # String representation of the object
    
    def deposit(self,amount): # Method to deposit money into the account
        if amount > 0: # Check if it is positive
            self.account += amount # Add the amount to the account balance
            print(f"{amount} deposited. New balance: {self.account}")  # Print the new balance
        else: # If not positive
            print("Please deposit a positive number.") # Print error message if deposit amount is not positive
    
    def withdraw(self,amount): # Method to withdraw money from the account
        if amount < 0: # Check if the withdrawal amount is negative
            print("Please withdraw an amount greater than zero.") # Print error message if amount is negative
        elif amount > self.account: # Check if it exceeds the account balance
            print("Insufficient funds.") # Print error message if insufficient funds
        else: # If it is valid
            self.account -= amount # Subtract the withdrawal amount from the account balance
            print(f"{amount} withdrawn. New balance: {self.account}") # Print the new balance
            
    def check_balance(self): # Method to check the account balance
        print(f"Balance: {self.account}") # Print the account balance

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest1.py'))