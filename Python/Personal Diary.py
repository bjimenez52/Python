'''
Name: Bianca Jimenez
github link: https://github.com/bjimenez52/Python/tree/main/Python
Create a Python program that functions as a personal diary. 
Users should be able to add entries with the date and time they provide, 
which are then saved to a file.
Test the program using the command, type diary.txt to check the contents of the diary.
'''

# This function allows the user to write diary entries with a timestamp
def main():
    # Prompt the user for the current date and time
    date_time = input("Enter the current date and time (e.g., YYYY-MM-DD HH:MM): ")
    
    # Prompt the user for their diary entry
    diary_entry = input("Enter your diary entry: ")
    
    # Open or create the diary.txt file in append mode using open() method
    diary_file = open("diary.txt", "a")  # 'a' mode opens the file for appending
    
    # Write the date and time to the file
    diary_file.write(date_time + "\n")
    
    # Write the diary entry to the file
    diary_file.write(diary_entry + "\n")
    
    # Write a blank line to separate entries
    diary_file.write("\n")
    
    # Close he file using close() method
    diary_file.close()

# Ensure the main function runs when the script is executed
if __name__ == "__main__":
    main()