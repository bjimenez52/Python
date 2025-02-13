'''
Homework11
Name: Bianca Jimenez
github link: https://github.com/bjimenez52/Python/tree/main/Python
'''

def count_zeros(lst):
    # How many zeros are in the list of lists
    # Count_zeros([[0,1,0],[4,8,9,3,0],[0,0]]) -> Output 5
    # Count_zeros([[2,1,7],[4,8,3,0],[1,0],[5,9,7,0,1]]) -> Output 3
    # lst is the list of lists
    # i is the sublist
    # j is the element in the sublist  
    return sum([1 for i in lst for j in i if j == 0]) # return the sum of the number of zeros in the list of lists
    

def replace_with_zero(lst):
    # Replace all negative numbers with 0
    # Replace_with_zero([[-1,8,9],[5,1,-7],[10,-17,-8]]) -> Output [[0, 8, 9], [5, 1, 0], [10, 0, 0]]
    # Replace_with_zero([[4,8,9,-17,-8,3],[5,1,-7],[111,10,-17,8],[-91,5,-8,0,23],[-9,2]]) -> Output [[4, 8, 9, 0, 0, 3], [5, 1, 0], [111, 10, 0, 8], [0, 5, 0, 0, 23], [0, 2]]
    # i is the sublist
    # j is the element in the sublist
    for i in range(len(lst)): # iterate through the list
        for j in range(len(lst[i])): # iterate through the sublists
            if lst[i][j] < 0: # if the element is less than 0
                lst[i][j] = 0 # replace it with 0
    return lst # return the list with the replaced elements

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest11.py'))