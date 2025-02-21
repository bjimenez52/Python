'''
Homework13
Name: Bianca Jimenez
github link: https://github.com/bjimenez52/Python/tree/main/Python
'''
principal_amount = 0  # Principal amount
interest_rate = 0  # Rate as a percentage
times_compounded_per_year = 0  # Times compounded per year
number_of_years = 0  # Number of years

p = principal_amount
r = interest_rate # decimal
n = times_compounded_per_year
t = number_of_years

# Functions are defined here

# Function to calculate the simple interest
def calculate_interest(p, r, t):
    interest = p * r * t # Simple interest formula
    sum = interest # Total amount
    return round(sum,) 

# Function to calculate the compound interest
def compound_interest(p, r, n, t):
    a = p * (1 + (r / n)) ** (n * t) # Compound interest formula
    sum = a - p # Total amount
    return round(sum, 2)


if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest13.py'))