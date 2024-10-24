
# first creating a dictionary were the month numbers are the keys and days are the values 
month_days = {
    1: 31,  
    2: 28,  
    3: 31,  
    4: 30,  
    5: 31,  
    6: 30,  
    7: 31,  
    8: 31,  
    9: 30,  
    10: 31, 
    11: 30, 
    12: 31  
}

# Ask the user what month they want to know the days of
month = int(input("Enter the month (1-12): "))

# Checking if the input the user put is valid
if 1 <= month <= 12: #inorder to seperate febuarary
    if month == 2:  # this specifally has to ask in febuarary in order to ask if it is a leap year or not
        # Asking the user if the year is a leap year or not
        is_leap_year = input("Is the year a leap year? (yes/no): ").lower() #.lower() is used to remove case sensitivity
        if is_leap_year == 'yes': 
            print("February has 29 days.") #this is the out put if it is a leap year
        else:
            print("February has 28 days.") #otherwise this is the output 
    else:
        # Output the number of days for the month if the user didnt input febuarary
        days = month_days[month]
        print("The month ", {month}," has ",{days}, " days.")
else:
    print("its just between months between 1 - 12, try again" ) #this is the output if the user inputs a number that isint 1 - 12
