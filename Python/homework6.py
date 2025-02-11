'''
Homework6
Name: Bianca Jimenez
github link: https://github.com/bjimenez52/Python/tree/main/Python
'''

def div_by_seven(num):
# Is the number divisible by 7?
# If so, return the number divided by 7
# If not, return the number minus 1
# >>> div_by_seven(8)
# 7
# >>> div_by_seven(30)
# 7, 14, 21, 28
     for number in range(1, num+1):
        if number % 7 == 0:
            print(number)
    

def squares_of_numbers(num):
# Return the square of the numbers from 1 to the given number
# >>> squares_of_numbers(2)
# 1
# >>> squares_of_numbers(3)
# 1, 4
# >>> squares_of_numbers(5)
# 1, 4, 9, 16

    for i in range(1, num):
        print(i**2)
    return 

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest6.py'))