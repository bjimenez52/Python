'''
Homework18
Name: Bianca Jimenez
github link: https://github.com/bjimenez52/Python/tree/main/Python
'''

# Check if the number is in the dictionary
def iterate_dictionary(lst): 
    dict = {1:"one",2:"two",3:"three"} # dictionary
    for num in lst: # iterate through list
        try: # try to print
            print(dict[num]) # print number
        except: # if number is not in dictionary
            print("Number not in dictionary") # print number not in dictionary
    return
# Check if the number is positive
def check_if_positive(lst): 
    for num in lst: # iterate through list
        if num > 0: # check if positive
            print(num) # print positive
        else: # if not positive
            print("not positive") # print not positive
    return
# Division
def division(lst): 
    num = 0 # initialize num
    for num in lst: # iterate through list
        try: # try to divide
            print(round(100/num,2)) # print division
        except: # if can't divide
            print("can't divide by zero") # print can't divide
    return 

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest18.py'))