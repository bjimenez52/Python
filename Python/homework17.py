'''
Homework17
Name: Bianca Jimenez
github link: https://github.com/bjimenez52/Python/tree/main/Python
'''

# frequency counter function
def frequency_counter(lst): # function to count the frequency of the elements in the list
    frequency = {} # empty dictionary
    for i in lst: # loop through the list
        if i in frequency: # if the element is in the dictionary
            frequency[i] += 1 # increment the value of the element
        else: # if the element is not in the dictionary
            frequency[i] = 1 # add the element to the dictionary
    # print the frequency of the elements from the list in a dictionary format        
    print('{'+','.join(f'{key}:{value}' for key, value in frequency.items())+'}') 
  
def translation(english_words):
    # Step 1: Create the NATO Phonetic Alphabet Dictionary
    # define nato_alphabet as a dictionary with each English alphabet letter as a key and its NATO phonetic term as the value
    nato_alphabet = {
        "A": "Alfa", "B": "Bravo", "C": "Charlie", "D": "Delta", "E": "Echo", "F": "Foxtrot", "G": "Golf",
        "H": "Hotel", "I": "India", "J": "Juliett", "K": "Kilo", "L": "Lima", "M": "Mike", "N": "November",
        "O": "Oscar", "P": "Papa", "Q": "Quebec", "R": "Romeo", "S": "Sierra", "T": "Tango", "U": "Uniform",
        "V": "Victor", "W": "Whiskey", "X": "X-ray", "Y": "Yankee", "Z": "Zulu"
    }
    english_words = english_words.upper()
    print('\n'.join([nato_alphabet[letter] for letter in english_words if letter in nato_alphabet]))
    # Step 2: Develop the Spelling Program
    # define a function called spell_word():
    def spell_word():
        # prompt the user to enter a word and store it in 'user_word'
        # convert'user_word' to uppercase to match dictionary keys
        user_word = input("Enter a word: ")
        user_word = user_word.upper()
        # for each letter in 'user_word' find the corresponding NATO phonetic term in nato_alphabet
        for letter in user_word:
            if letter in nato_alphabet:
                print(nato_alphabet[letter]) 
        return 
    # Step 3: Incorporate a Main Function
    # define a function called main():
    def main():
        # call the spell_word function
        spell_word()
    # Step 4: Test Program
    # call the main function
    if __name__ == '__main__':
        main()

if __name__ == "__main__":       
    import doctest
    print(doctest.testfile('doctest17.py'))