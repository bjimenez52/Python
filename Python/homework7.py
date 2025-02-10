'''
Homework7
Name: Bianca Jimenez
github link: https://github.com/bjimenez52/Python/tree/main/Python
'''


def fizzbuzz(num):
    # Print fizz if the number is divisible by 3
    # Print buzz if the number is divisible by 5
    # Print fizzbuzz if the number is divisible by both 3 and 5
    # If the number is not divisible by either 3 or 5, print the number itself
    for num in range(1,num+1):
        if num%3==0 and num%5==0:
            print("FizzBuzz")
        elif num%3==0:
            print("Fizz")
        elif num%5==0:
            print("Buzz")
        else:
            print(num)
    return 

def scholarship_eligibility(gpa,credits):
    # A student is eligible for scholarship if the gpa is greater than 3.5 and the credits are greater than 60
    # return True if the student is eligible for scholarship
    # return False if the student is not eligible for scholarship
    if gpa>3.5 and credits>60:
        return True
    else:
        return False
    return

def max_of_three_numbers(num1,num2,num3):
    # Return the maximum of the three numbers
    return max(num1,num2,num3)

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest7.py'))