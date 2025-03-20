'''
Homework24
Name: Bianca Jimenez
github link: https://github.com/bjimenez52/Python/tree/main/Python
'''

# Function that takes a list of flowers and an index to then print the flower at that index
def flowers(idx,list_of_flowers):
    try: # Try block to catch exceptions
        if not isinstance(idx, int): # Check if the input is an integer
            raise TypeError("Invalid input! Please enter a number.") # Raise an exception if the input is not an integer
        if idx < -1 or idx > len(list_of_flowers): # Check if the index is out of range
            raise IndexError("Number out of range! Please choose a valid flower number.") # Raise an exception if the index is out of range 
        print(f"You selected: {list_of_flowers[idx]}") # Print the flower at the index
    # Catch exceptions
    except TypeError as te: # Catch TypeError
        print(te) # Print the error message
    except IndexError as ie: # Catch IndexError
        print(ie) # Print the error message


if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest25.py'))