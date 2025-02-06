
'''
Homework5
Name: Bianca Jimenez
github link: https://github.com/bjimenez52/Python/tree/main/Python
'''

def collatz_conjecture(num):
    # Is the number even or odd?
    # If the number is even, divide it by two. 
    # If the number is odd, triple it and add one.
    # Repeat the process with the new number until you reach 1.
    num = int(input("Enter a number: "))
    while num != 1:
        print(num)
        if num % 2 == 0:
            num = num // 2
        else:
            num = num * 3 + 1
    print(num)
    return 

def add_numbers(num): 
    # Add all numbers from integer 1 to the given number.
    total = int(input("Enter a positive integer: "))
    for i in range(-1, total - 1):
        total += i 
    print(total)
    return 


if __name__ == "__main__":
    collatz_conjecture(6)
    collatz_conjecture(18)
    add_numbers(10)
    add_numbers(25)
    # import doctest
    # print(doctest.testfile('doctest5.py'))