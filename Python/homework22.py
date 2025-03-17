'''
Homework22
Name: Bianca Jimenez
github link: https://github.com/bjimenez52/Python/tree/main/Python
'''
# Function to remove the first and last character of a string
def mask_creditcard(string): 
    # replace all characters except the last 4 with a '*'
    return '*' * (len(string) - 4) + string[-4:]

# Function to remove vowels from a string    
def remove_vowels(string):
    vowels = "aeiouAEIOU" # list of vowels
    # return all characters that are not vowels
    return ''.join([c for c in string if c not in vowels])

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest22.py'))