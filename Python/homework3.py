'''
Homework3
Name: Bianca Jimenez
github link: https://github.com/bjimenez52/Python/tree/main/Python
'''

def positive_or_negative(num):
    # Loop through list to check if positive or negative 
    if num >= 0:
        print("True")
    else:
        if num < 0:
            print("False")

    # List of ages for users        
    num = (10, -3)
    return 

def is_able_to_drive(num):
    # Loop through list to check if user is old enough to drive
    if num >= 16:
        return(True)
    else:
        return(False)
    
    # List of ages for users
    num = (15, 18, 13, 25)
    return

def is_able_to_vote(num):
    # Loop through list to check if user is old enough to vote
    if num >= 18:
        return(True)
    else:
        return(False)
    
    # List of ages for users
    num = (8, 28)
    return

def can_buy_alcohol(num):
    # Loop through list to check if user is old enough to buy alcohol
    if num >= 21:
        return(True)
    else:
        return(False)  
    
    # List of ages for users
    num = (23, 16)
    return 

def senior_discount(num):
    # Loop through list to check if user is old enough to get a senior discount
    if num >= 65:
        return(True)
    else:
        return(False)
    
    # List of ages for users
    num = (72, 54)
    return 

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest3.py'))