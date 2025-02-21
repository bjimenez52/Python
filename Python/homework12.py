'''
Homework12
Name: Bianca Jimenez
github link: https://github.com/bjimenez52/Python/tree/main/Python
'''

# Function Definitions
# Two functions are defined in this file: rectangle and circle
# rectangle takes two arguments: side1 and side2
# circle takes one argument: radius
def rectangle(side1, side2):
    # Calculate the area of a rectangle
    area = side1 * side2
    print("'The area of the rectangle is " + str(area) + " square units'")

def circle(radius):
    # Calculate the area of a circle
    pi = 3.14 # approximate value of pi
    # Calculate the area of a circle using the formula
    area = pi * radius * radius 
    # Round the area to 2 decimal places
    area = round(area, 2)
    print("'The area of a circle is " + str(area) + " square units'")

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest12.py'))