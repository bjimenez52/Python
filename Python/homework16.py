'''
Homework16
Name: Bianca Jimenez
github link: https://github.com/bjimenez52/Python/tree/main/Python
'''

# Implementing the pythagorean theorem using a tuple
def pythagorean_thm(tuple): # tuple that has two numbers: a and b
   tuple = tuple 
   a = tuple[0] # a is the first number in the tuple
   b = tuple[1] # b is the second number in the tuple
   c = (a**2 + b**2)**0.5 # c is the square root of a**2 + b**2
   if c == int(c): # if c is an integer, return c as an integer
       return int(c) 
   else:
       return round(c,2) # if c is not an integer, return c as a float with 2 decimal places
   
# Implementing the distance between two points using tuples
def distance_between_points(tuple1,tuple2): # two tuples that each have two numbers (x,y)
    tuple1 = tuple1
    tuple2 = tuple2
    x1 = tuple1[0] # x1 is the first number in the first tuple
    y1 = tuple1[1] # y1 is the second number in the first tuple
    x2 = tuple2[0] # x2 is the first number in the second tuple
    y2 = tuple2[1] # y2 is the second number in the second tuple
    distance = ((x2-x1)**2 + (y2-y1)**2)**0.5 # distance is the square root of (x2-x1)**2 + (y2-y1)**2
    if distance == int(distance): # if distance is an integer, return distance as an integer
        return int(distance)
    else:
        return round(distance,2) # if distance is not an integer, return distance as a float with 2 decimal places
    
if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest16.py'))