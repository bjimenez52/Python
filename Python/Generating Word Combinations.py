'''
Name: Bianca Jimenez
github link: https://github.com/bjimenez52/Python/tree/main/Python
'''

# Function to generate two-letter combinations
def two_letter_combinations(characters): 
    
    '''
    Generate function to produce all two-letter combinations from a given list of characters.
    '''

    # Iterate over list of characters for first letter
    for first in characters:
        # Iterate over list of characters for second letter
        for second in characters:
            # Concatenate first and second letters to form a combination
            yield first + second

# The main function to execute the generator and print combinations
def main():
    # Define a list of five characters
    characters = ['a', 'b', 'c', 'd', 'e']

    # Call genertor function and iterate through the combinations
    for combination in two_letter_combinations(characters):
        # Print each combination
        print(combination)

# Entry point of the script
if __name__ == "__main__":
    main()