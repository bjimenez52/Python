'''
Homework2
Name: Bianca Jimenez
github link: https://github.com/bjimenez52/Python/tree/main/Python
'''

# Define inches to centimeters
inches_1 = 2
cm_value_1 = 5.08
# Conversion factor: 1 inch = 2.54 centimeters 
conversion_factor = 2.54
inches_1 = cm_value_1 /conversion_factor
print(f"{inches_1} inches is equal to {cm_value_1} centimeters.")

# Define feet to meters
feet_value_1 = 3
meters_value_1 = 0.91
# Conversion factor: 1 foot = 0.3048 meters
conversion_factor = 0.3048
feet_value_1 = meters_value_1 / conversion_factor
print(f"{feet_value_1:.1f} feet is equal to {meters_value_1:.2f} meters.")

# Define pounds to kilograms
lbs_value_1 = 2.7
kg_value_1 = 1.22
# Conversion factor: 1 pound = 2.20462 kilograms
conversion_factor = 2.20462
lbs_value_1 = kg_value_1 * conversion_factor
print(f"{lbs_value_1:.1f} pounds is equal to {kg_value_1:.2f} kilograms.")

# Define hours to minutes
hours_value_1 = 2.5
hours_value_2 = 3.65
minutes_value_1 = 150.0
minutes_value_2 = 219.0
# Conversion factor: 1 hour = 60 minutes
conversion_factor = 60
hours_value_1 = minutes_value_1 / conversion_factor
hours_value_2 = minutes_value_2 / conversion_factor
print(f"{hours_value_1} hours is equal to {minutes_value_1:.1f} minutes.")
print(f"{hours_value_2} hours is equal to {minutes_value_2:.1f} minutes.")    