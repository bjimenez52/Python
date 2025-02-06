'''
Homework4
Name: Bianca Jimenez
github link: https://github.com/bjimenez52/Python/tree/main/Python
'''

def grade_calculator(score):
    # What is the grade of the student?
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    elif 0 <= score < 60:
        return 'F'
    else:
        return 'Enter a grade between 0-100'
    
    # List of grades
    grades = (95, 83, 49, -5, 102)
    return
   
def even_or_odd(num):
    # Check if the number is even or odd
    if num % 2 == 0:
        return 'even'
    else:
        return 'odd'
    
    # List of numbers
    num = (5, 2)
    return 



if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest4.py'))