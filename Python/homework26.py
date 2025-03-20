'''
Homework24
Name: Bianca Jimenez
github link: https://github.com/bjimenez52/Python/tree/main/Python
'''

def dictionary_exceptions(key,dict): # Function to check the key of a dictionary
    try: # try block to check the key
        price = dict[key] # price of the key
        print(f"The price of {key} is ${price}") # print the price of the key
    except KeyError: # if the key is not found
        print("Error: Flower not found! Please enter Rose, Lily, or Tulip.") # print the error message

def string_exceptions(idx,str): # Function to check the index of a string
    try: # try block to check the index
        characer = str[idx] # character at the index
        print(f"The character at index {idx} is: {characer}") # print the character at the index
    except ValueError: # if the index is not a number
        print("Error: Please enter a valid number for the index.") # print the error message
    except IndexError: # if the index is out of range
        print("Error: Index out of range! Please enter a valid index.") # print the error message
    except TypeError as te: # if the index is not an integer
        print("Error: String indices must be integers, not 'str'") # print the error message


if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest26.py'))