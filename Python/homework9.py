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
    for i in range(n): # iterate through the list
        for j in range(0, n-i-1): 
            if lst[j] > lst[j+1]: # if the current element is greater than the next element
                lst[j], lst[j+1] = lst[j+1], lst[j] # swap the elements
    return lst # return the sorted list

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest9.py'))