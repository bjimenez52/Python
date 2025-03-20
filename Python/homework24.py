'''
Homework24
Name: Bianca Jimenez
github link: https://github.com/bjimenez52/Python/tree/main/Python
'''

# Function to Validate a Password
def is_valid_password(word): 
    if not (8 <= len(word) <= 20): # checks if the length of the word is between 8 and 20 characters
        return False # returns False if the length of the word is not between 8 and 20 characters
    if not any(char.isupper() for char in word): # checks if there is at least one uppercase letter
        return False # returns False if there is no uppercase letter
    if not any(char.islower() for char in word): # checks if there is at least one lowercase letter
        return False # returns False if there is no lowercase
    if not any(char.isdigit() for char in word): # checks if there is at least one number
        return False # returns False if there is no number
    if not any(char in "!@#$%^&*()-+" for char in word): # checks if there is at least one symbol
        return False # returns False if there is no symbol
    return True # returns True if all conditions are met

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest24.py'))