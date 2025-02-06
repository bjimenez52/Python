'''
Homework2
Name: Bianca Jimenez
github link: https://github.com/bjimenez52/Python/tree/main/Python
'''

def birthday(month,day,year):
    # When is your birthday?
    '''inputs: month, day, year
    outputs: string
    description: This function takes in the month, day, and year of your birthday and returns a string that states your birthday.
    '''
    return 'Your birthday is ' + month + ' ' + str(day) + ', ' + str(year) + '.'

def address(street,city,state,zipcode):
    # What is your address?
    '''inputs: street, city, state, zipcode
    outputs: string
    description: This function takes in the street, city, state, and zipcode of your address and returns a string that states your address.
    '''
    return 'Your address is ' + street + ', ' + city + ', ' + state + ', ' + str(zipcode) + '.'

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest25.py'))