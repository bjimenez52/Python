'''
Homework1
Name:
github link: 
'''

def add(num1,num2):
    # add two numbers
    sum = num1 + num2
    return sum 

def subtract(num1,num2):
    # subtract two numbers
    diff = num1 - num2
    return diff

def multiply(num1,num2):
    # prduct of two numbers
    product = num1 * num2
    return product

def division(num1,num2):
    # quotient of two numbers
    quotient = num1 / num2
    return quotient

def int_div(num1,num2):
    # interger division of two numbers
    int_div = num1 // num2
    return int_div

def modulus(num1,num2):
    # remainder of two numbers
    remainder = num1 % num2
    return remainder

def exp(num1,num2):
    # exponent of two numbers
    exp = num1 ** num2
    return exp

def area(length,width):
    # area of a rectangle
    area = length * width
    return ('The area of the rectangle with a length of {} and a width of {} is {}'.format(length,width,area))


if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest1.py'))