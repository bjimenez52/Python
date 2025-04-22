'''
1. Open the file sales_totals in read mode
2. Read in all the lines using a loop
3. Strip the newline symbol and convert each line to a float
4. Add each number to the running total
5. Count the number of lines
6. Format and display each number
7. Outside of the loop, format and display the total, the count, and the average
8. Do this using a main function 
9. Use try and except statements to handle file errors
Name: Bianca Jimenez
github link: https://github.com/bjimenez52/Python/tree/main/Python
'''

# Function reads sales data from a file and calculates total, count, and average sales
def main(): 
    # Initialize variables
    total = 0.0
    count = 0
    
    try: 
        # Open the sales_totals.txt.py file for reading
        with open("sales_totals.txt.py", "r") as file:
            # Read each line in the file
            for line in file:
                try:
                    # Strip newline and convert to float
                    number = float(line.strip())
                
                    # Add to the running total
                    total += number
                
                    # Increment the count of lines
                    count += 1
                
                    # Format and display each number
                    print(f"Sales amount: ${number:.2f}")
                # Handle conversion errors
                except ValueError as e: 
                    print(f"Warning: Could not convert line to float: {line.strip()} - {e}") 

        # Calculate the average if count is not zero
        if count > 0:
            average = total / count
            # Format and display the total, count, and average
            print(f"\nTotal Sales: ${total:.2f}")
            print(f"Number of Sales: {count}")
            print(f"Average Sale: ${average:.2f}")
        # If no valid sales data was found
        else: 
            print("No sales data to process.")
    # Handle file not found error
    except FileNotFoundError:
        print(f"Error: The file 'sales_totals.txt.py' was not found.")
    # Handle other IO errors
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Ensure the main function runs when the script is executed
if __name__ == "__main__":
    main()