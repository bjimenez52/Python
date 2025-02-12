'''
Homework10
Name: Bianca Jimenez
github link: https://github.com/bjimenez52/Python/tree/main/Python
'''

def find_missing_number(lst):
# Find the missing numbers in the list
# lst: list of integers
    if not lst: 
        return [] 
  
    min_num = 0 # Start from 0
    max_num = max(lst) # Find the maximum number in the list
    full_list = list(range(min_num, max_num + 1)) # Create a range of numbers from 0 to max_num
    missing_numbers = sorted(set(full_list) - set(lst)) # Find the missing numbers by subtracting the full list from the given list

    return missing_numbers 

def even_partition(lst):
# Return a list of even numbers from the given list
# lst: list of integers
# num: integer
    return [num for num in lst if num % 2 == 0]

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest10.py'))