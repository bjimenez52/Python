# calculate a person's age in: Years, months, weeks, days
# 30.41 days in a month
# 7 days in a week 

from datetime import datetime # import datetime module

def main(): # main function
   
    print("\n\n") # print new lines 
    try:
        today = datetime.today() # get today's date
        birth_year = int(input("What year were you born?  ")) # get year of birth
        month = int(input("What Month were you born (as a number. May would be 5)  ")) # get month of birth
        day = int(input("What day of the month were you born?  ")) # get day of birth
        # just need datetime not datetime.date
        # because we imported datetime from datetime
        birthday = datetime(birth_year, month, day) # create a datetime object for birthday
        print("Your birthday is: ") # print birthday
        
        birthday_output = birthday.strftime("%Y-%m-%d") # format birthday as YYYY-MM-DD
        print(birthday_output) # print formatted birthday

        delta = today - birthday # calculate the difference between today and birthday
        print(f'Difference is {delta.days} days') # print difference in days
        
        delta_years = delta.days // 365.2425 # calculate years (using average year length)
        print(f'You are {delta_years} years old') # print years old
        remaining_days = delta.days % 365.2425 # calculate remaining days after years

        delta_months = remaining_days // 30 # calculate months (using average month length)
        remaining_days_after_months = remaining_days % 30 # calculate remaining days after months
        delta_weeks = remaining_days_after_months // 7 # calculate weeks (using average week length)
        delta_days = remaining_days_after_months % 7 # calculate remaining days after weeks
       
      
    except Exception as e: # catch any exceptions
        print(f"ooooops!!!:  {e}") # print error message
        main() # call main function again if there is an error
main() # call main function to start the program