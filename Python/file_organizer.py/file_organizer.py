import os

main_directory = 'MyFiles' # Main directory name
subdirectories = ['Docs', 'Images', 'Videos'] # List of subdirectory names

def main(): # Main function to create directories
    try:
        os.mkdir(main_directory) # Create the main directory
        print(f"Directory '{main_directory}' created.")
    except FileExistsError: # If the directory already exists
        print(f"Directory '{main_directory}' already exists.")

    for subdirectory in subdirectories: # Create subdirectories
        path = os.path.join(main_directory, subdirectory) # Join the main directory with the subdirectory name
        try:
            os.mkdir(path) # Create the subdirectory
            print(f"Subdirectory '{subdirectory}' created inside '{main_directory}'.")
        except FileExistsError: # If the subdirectory already exists
            print(f"Subdirectory '{subdirectory}' already exists inside '{main_directory}'.")

main() # Call the main function to execute the code