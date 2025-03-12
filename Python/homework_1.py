'''
Homework1
Name: Bianca Jimenez
github link: https://github.com/bjimenez52/Python/tree/main/Python
'''

import random

def check(guess, actual_number): # function to check if guess is close to actual number
    difference = abs(guess - actual_number) # calculate difference between guess and actual number
    # return result based on difference
    if difference < 5: 
        return("Very Hot")
    elif difference < 15: 
        return("Hot")
    elif difference < 25:
        return("Cool")
    else:
        return("Cold")
   
def main(actual_number): # function to run guessing game
    actual_number = random.randint(1, 100) # generate random number between 1 and 100
    
    while True: # loop until user guesses correct number
        try:
            guess = int(input("Guess a number between 1 and 100: ")) # user input
            if guess < 1 or guess > 100: # check if guess is within range
                print("Please enter a number between 1 and 100") 
                continue

            if guess == actual_number: # check if guess is correct
                print("You Got It!")
                break # exit loop
            
            print(check(guess, actual_number)) # print result of check function
            
        except ValueError: # check if input is a number
            print("Invalid input. Please enter a valid number.") 
            
            

if __name__ == "__main__":
    import doctest
    doctest.testfile('doctest1.py')
