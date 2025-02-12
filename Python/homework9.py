'''
Homework9
Name: Bianca Jimenez
github link: https://github.com/bjimenez52/Python/tree/main/Python
'''

def bubble_sort(lst):
    # Bubble sort algorithm
    # lst: list of integers
    # Bubble Sort One: bubble_sort([42, 17, 94, 8, 65, 39, 13, 77, 21, 56]) -> [8, 13, 17, 21, 39, 42, 56, 65, 77, 94]
    # Bubble Sort Two: bubble_sort([29, 6, 96, 15, 48, 100, 81, 72, 22, 37]) -> [6, 15, 22, 29, 37, 48, 72, 81, 96, 100]
    # Bubble sort Three: bubble_sort([16, 52, 85, 50, 5, 79, 67, 60, 59, 60]) -> [5, 16, 50, 52, 59, 60, 60, 67, 79, 85]
    n = len(lst) # length of the list
    swapped = True # set swapped to True

    # Continue to iterate through the list until no more swaps are needed
    while swapped: # while swapped is True
        swapped = False # Reset the flag at the beginning of each iteration
        for i in range(n-1): # iterate through the list
            if lst[i] > lst[i+1]: # if the current element is greater than the next element
                lst[i], lst[i+1] = lst[i+1], lst[i] # swap the elements
                swapped = True # set swapped to True

    # Print the sorted list
    print(lst)
    return 

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest9.py'))