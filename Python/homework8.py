'''
Homework8
Name: Bianca Jimenez
github link: https://github.com/bjimenez52/Python/tree/main/Python
'''

def sum_numbers(lst):
    # Add all the numbers in a given list
    # >>> sum_numbers([1, 2, 3])
    # 6
    # >>> sum_numbers([1, 25, 36, 2, 15])
    # 79
    return sum(lst)

def largest_number(lst):
    # Find the largest number in a given list
    # >>> largest_number([1, 2, 3])
    # 3
    # >>> largest_number([9, 2, 17, 26, 8])
    # 26
    # >>> largest_number([1, 98, 65, 14, 23, 47])
    # 98
    return max(lst)

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest8.py'))
