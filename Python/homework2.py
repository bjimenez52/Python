'''
Homework2
Name: Bianca Jimenez
github link: https://github.com/bjimenez52/Python/tree/main/Python
'''

def inches_to_cm(inches):
    # 1 inch = 2.54 cm
    # Conversion factor 1 inch = 2.54 cm
    # inches = 2
    # cm_value = 5.08
    conversion_factor = 2.54
    cm_value = inches * conversion_factor
    return cm_value

def feet_to_meters(feet):
    # 1 foot = 0.3048 meters
    # Conversion factor 1 foot = 0.3048 meters
    # feet = 3
    # meters = 0.91
    conversion_factor = 0.3048
    meters = feet * conversion_factor
    f"{meters:.2f}"
    string_value = f"{meters:.2f}"
    float_value = float(string_value)
    return float_value

def lbs_to_kg(lbs):
    # pounds to kilograms
    # Conversion factor 1 pound = 0.453592 kilograms
    # lbs = 2.7
    # kg = 1.22
    conversion_factor = 0.453592
    kg = lbs * conversion_factor
    f"{kg:.2f}"
    string_value = f"{kg:.2f}"
    float_value = float(string_value)
    return float_value

def hours_to_minutes(hrs):
    # hours to minutes
    # Conversion factor 1 hour = 60 minutes
    # hrs = 2.5, 3.65
    # minutes = 150.0, 219.0
    conversion_factor = 60
    minutes = hrs * conversion_factor
    return minutes    

if __name__ == "__main__":
    import doctest
    print(doctest.testfile('doctest2.py'))