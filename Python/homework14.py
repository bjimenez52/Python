'''
Homework14
Name: Bianca Jimenez
github link: https://github.com/bjimenez52/Python/tree/main/Python
'''

# Write a program that calculates the Body Mass Index (BMI) 
# Global variables are: 
# 1. CONVERT WEIGHT FROM POUNDS TO KILOGRAMS (1 POUND = 0.453592 KILOGRAMS)
# 2. CONVERT HEIGHT FROM INCHES TO METERS (1 INCH = 0.0254 METERS)
global weight_kg
weight_kg = 0.453592
global height_m
height_m = 0.0254

def convert_to_kg(lbs):
    # Convert weight from pounds to kilograms
    # 1 pound = 0.453592 kilograms
    # 'kg' is a local variable
    # Use the global variable 'weight_kg'
    kg = lbs * weight_kg
    return round(kg,2)

def convert_to_meters(inches):
    # Convert height from inches to meters
    # 1 inch = 0.0254 meters
    # 'm' is a local variable
    # Use the global variable 'height_m'
    m = inches * height_m
    return round(m,2)

def bmi_calculation(lbs,height):
    weight_kg = convert_to_kg(lbs) 
    height_m = convert_to_meters(height)
    # Calculate the Body Mass Index (BMI)
    bmi = weight_kg / (height_m * height_m) # Formula for bmi
    bmi = round(bmi,2) # Round to two decimal places
    # Determine the weight status
    if bmi < 18.5:
        print('"underweight"')
    elif bmi >= 18.5 and bmi < 24.9:
        print('"normal weight"')
    elif bmi >= 25 and bmi < 29.9:
        print('"overweight"')
    else:
        print('"obese"')    
        
    
if __name__ == "__main__":

    # Input from users
    while True:
        try:
            weight_lbs = float(input("Enter your weight in pounds: "))
            if weight_lbs < 0:
                print("Invalid input. Please enter a positive number.")
                continue
            height_inches = float(input("Enter your height in inches: "))
            if height_inches < 0:
                print("Invalid input. Please enter a positive number.")
                continue
            print(bmi_calculation(weight_lbs,height_inches))
            break
        except ValueError:
            print("Invalid input. Please enter numerical values.")
    
    import doctest
    print(doctest.testfile('doctest14.py'))

    