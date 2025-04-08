'''
Part 1: Defining Classes

File 1: Write an Employee class with the following attributes:
Employee name
Employee number
Create a subclass named ProductionWorker that inherits from Employee. This subclass should include additional attributes:
Shift number (integer: 1 for day, 2 for night)
Hourly pay rate
Implement accessor and mutator methods (getters and setters) for each class.


Part 2: Implementing and Testing
 
Part 2: Write a script to:
Create an instance of ProductionWorker.
Prompt the user for each attribute's data.
Store and then display the data using the object's methods.

Name: Bianca Jimenez
github link: https://github.com/bjimenez52/Python/tree/main/Python
'''

# Class: Employee
class Employee: 
    def __init__(self, name, number): # Constructor with parameters
        self.name = name # Instance variable for name
        self.number = number # Instance variable for number
    
    # Accessor Methods for Getters
    def get_name(self): # Accessor method 
        return self.name
    def get_number(self): # Accessor method 
        return self.number

# Class: ProductionWorker
class ProductionWorker(Employee):
    def __init__(self, name, number, shift, hourly_rate): # Constructor with parameters
        super().__init__(name, number) # Call the constructor of the base class
        self.shift = shift # Instance variable for shift (1 for day, 2 for night)
        self.hourly_rate = hourly_rate # Instance variable for hourly rate

    # Accesor Methods for Getters
    def get_shift(self): # Accessor method
        return self.shift 
    def get_hourly_rate(self): # Accessor method
        return self.hourly_rate
    
    # Mutator Methods for Setters
    def set_shift(self, shift): # Mutator method
        self.shift = shift
    def set_hourly_rate(self, hourly_rate): # Mutator method
        self.hourly_rate = hourly_rate

# Main Function to Demonstrate the Classes
def main(): 
    # Prompt User for Employee Details
    name = input("Enter employee's name: ") # Input for employee's name
    number = input("Enter employee's number: ") # Input for employee's number

    # Prompt User for ProductionWorker Details
    shift = int(input("Enter shift (1 for day, 2 for night): ")) # Input for shift
    hourly_rate = float(input("Enter hourly rate: ")) # Input for hourly rate

    # Create Instance of ProductionWorker
    worker = ProductionWorker(name, number, shift, hourly_rate)

    # Display Employee Details
    print("\nEmployee Details:") # Print header
    print(f"Name: {worker.get_name()}") # Print employee's name
    print(f"Number: {worker.get_number()}") # Print employee's number
    print(f"Shift: {'Day' if worker.get_shift() == 1 else 'Night'}") # Print shift (day or night)
    print(f"Hourly Rate: ${worker.get_hourly_rate():.2f}") # Print hourly rate formatted to 2 decimal places

if __name__ == "__main__": 
    main()