'''
Homework15
Name: Bianca Jimenez
github link: https://github.com/bjimenez52/Python/tree/main/Python
'''
# factorial function with recursion
def factorial(n): # define function with one parameter being n
    if n==1 or n==0: # base case 1 and 0
        return 1 # factorial of 1 and 0 is 1
    else:
        return factorial(n-1) * n # recursive case 

# main function 
def main(num1): # define function 
    num1 = int(num1) # convert to integer 
    print(f'"The factorial of {num1} is {factorial(num1)}."') # result of factorial 

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest15.py'))