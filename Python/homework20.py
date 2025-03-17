'''
Homework20
Name: Bianca Jimenez
github link: https://github.com/bjimenez52/Python/tree/main/Python
'''

# Function that converts a string to a list of ASCII values
def convert_to_ascii(string): 
    convert_to_ascii = [] # Create an empty list to store the ASCII values
    for i in string: # Iterate through the string
        convert_to_ascii.append(ord(i)) # Append the ASCII value of each character to the list
    if len(convert_to_ascii) == 1: # If the string has only one character, return the ASCII value as an integer
        return convert_to_ascii[0] # Return the ASCII value as an integer
    else:
        return convert_to_ascii # Return the list of ASCII values
 
# Function that filters out non-ASCII characters from a string    
def filter_non_ascii(string):
    # Return a string that contains only ASCII characters, excluding apostrophes
    return ''.join([char for char in string if ord(char) < 128])
   
if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest20.py'))