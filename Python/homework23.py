'''
Homework23
Name: Bianca Jimenez
github link: https://github.com/bjimenez52/Python/tree/main/Python
'''

# Function to group words by first letter
def group_by_first_letter(words): 
    grouped = {} # empty dictionary
    for word in words: # loop through the words
        first_letter = word[0].lower() # get the first letter of the word and convert to lowercase
        if first_letter not in grouped: # if the first letter is not in the dictionary
            grouped[first_letter] = [] # add the first letter as a key and an empty list as a value
        grouped[first_letter].append(word) # append the word to the list of the first letter
    return grouped

# Function to convert list of words to a sentence
def convert_to_sentence(words):
    return ' '.join(words) + "." # join the words with a space and add a period at the end

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest23.py'))