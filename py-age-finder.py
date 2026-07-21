from datetime import datetime

# get day, month and year information
birth_day = int(input("Enter your birth day (1-31): "))
birth_month = int(input("Enter your birth month (1-12): "))
birth_year = int(input("Enter your birth year: "))

# current date
today = datetime.now()

# calculate the approximate difference in years
age = today.year - birth_year

# month and day check:
# if the birth month hasn't arrived yet, or if we are in the birth month but the day hasn't arrived yet, we subtract 1 from the age
if (today.month < birth_month) or (today.month == birth_month and today.day < birth_day):
    age -= 1

print("Your real age:", age)