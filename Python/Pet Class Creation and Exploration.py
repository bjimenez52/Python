'''
1. Create the Pet Class:
Define a Pet class with attributes: kind (e.g., dog, cat), breed, and name.
Implement get and set methods for each of these attributes.
Add a method called print_details that prints the details of the pet.
2. Create Instances:
Create three objects of the Pet class with different kinds, breeds, and names.
Call the print_details method for each object that you created
3. Demonstrate a Special Method or Function:
Name: Bianca Jimenez
github link: https://github.com/bjimenez52/Python/tree/main/Python

'''
# Class Definition for Pet
class Pet: 
    def __init__(self, kind, breed, name): # Initialize the attributes
        self.kind = kind # Kind of pet (e.g., dog, cat, turtle)
        self.breed = breed # Breed of the pet (e.g., Chihuahua, American Shorthair, Red-eared Slider)
        self.name = name # Name of the pet (e.g., Iris, Nala, Bowser)
    
    # Get Methods for each Attribute
    def get_kind(self): # Get the kind of pet
        return self.kind
    
    def get_breed(self): # Get the breed of the pet
        return self.breed 
    
    def get_name(self): # Get the name of the pet
        return self.name
    
    # Set Methods for each Attribute
    def set_kind(self, kind): # Set the kind of pet
        self.kind = kind
    
    def set_breed(self, breed): # Set the breed of the pet
        self.breed = breed

    def set_name(self, name): # Set the name of the pet
        self.name = name

# Method to Print the Details of the Pet
    def print_details(self):
        print(f"Pet Details:\nKind: {self.kind}\nBreed: {self.breed}\nName: {self.name}") # End of class definition

# Create Instances of the Pet class
pet1 = Pet("Dog", "Chihuahua", "Iris") # Instance of pet1
pet2 = Pet("Cat", "American Shorthair", "Nala") # Instance of pet2
pet3 = Pet("Turtle", "Red-eared Slider", "Bowser") # Instance of pet3

# Call the print_details Method for each Pet Instance
pet1.print_details() # Print the details of pet1
pet2.print_details() # Print the details of pet2
pet3.print_details() # Print the details of pet3

# Demonstrate a Special Method or Function
print(f"Accessing the name of pet1: {pet1.get_name()}") # Access the name of pet1
print(f"Accessing the breed of pet2: {pet2.get_breed()}")  # Access the breed of pet2
print(f"Accessing the kind of pet3: {pet3.get_kind()}") # Access the kind of pet3