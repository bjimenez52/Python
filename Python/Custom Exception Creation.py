'''
Implement a custom exception class NotNumericError.
Write a Python script that prompts the user to input a number.
Use a try-except-else-finally block:
The try block should contain the logic to check if the input is a number. (isnumeric() )
The except block should catch the InvalidInputError and print an error message.
The else block should print a confirmation message if the input is valid.
The finally block should print a message indicating the end of the program's execution.
Ensure the program gracefully handles the exception and continues to prompt the user until a valid number is entered. (call the program again)
Name: Bianca Jimenez
github link: https://github.com/bjimenez52/Python/tree/main/Python

'''
# Custom Exception for Non-Numeric Values
class NotNumericError(Exception): 
    pass

# Function to Get User Input and Validation
def get_number_input(): 
    while True: # Loop until valid input is received
        user_input = input("Please enter a number: ") # Prompt user for input
        try: ## Try block to check if input is numeric
            if not user_input.isnumeric(): # Check if input is numeric
                raise NotNumericError("Input is not a number.") # Raise custom exception if not numeric
        except NotNumericError as e: # Catch the custom exception
                print(e) # Print error message
        else: # Else block executes if no exception is raised
            print(f"Thank you for entering a valid number: {user_input}") # Print confirmation message
            break # Exit the loop if input is valid
        finally: # Finally block executes regardless of exception
            print("End of input validation process.\n") # Print end message

# Call the Function to Test it
get_number_input()