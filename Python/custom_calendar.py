import calendar
import datetime

def main(): # This function generates a calendar for the user's birth month in the current year.
    current_year = datetime.datetime.now().year # Get the current year
    
    while True: 
        try: # Loop until a valid month is entered
            birth_month = int(input("Please enter your birth month (1-12): ")) # Prompt the user for their birth month
            if 1 <= birth_month <= 12: # Check if the input is a valid month
                break # Exit the loop if the input is valid
            else: # If the input is not a valid month, prompt the user again
                print("Invalid input. Please enter a number between 1 and 12.") # Error message
        except ValueError: # Handle non-integer inputs
            print("Invalid input. Please enter a valid integer.") # Error message
    
    # Generate and display the calendar for the given month and year
    print("\nHere is the calendar for month", birth_month, "in the year", current_year) # Display the selected month and year
    print(calendar.month(current_year, birth_month)) # Print the calendar for the specified month

# Call the main function
if __name__ == "__main__":
    main()