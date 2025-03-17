'''
Homework21
Name: Bianca Jimenez    
github link: https://github.com/bjimenez52/Python/tree/main/Python

'''
# Define the function
def is_palindrome(string): # function to check if a string is a palindrome
    # Normalize the string by removing spaces and converting to lowercase
    normalized_string = string.replace(" ", "").lower()
    # Check if the string is equal to its reverse
    return normalized_string == normalized_string[::-1]

# Define the function  
def is_anagram(string1,string2): # function to check if two strings are
    # Normalize the strings by removing spaces and converting to lowercase
    normalized_string1 = string1.replace(" ", "").lower()
    normalized_string2 = string2.replace(" ", "").lower()
    # Sort the characters of both strings and compare
    return sorted(normalized_string1) == sorted(normalized_string2)


if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest21.py'))