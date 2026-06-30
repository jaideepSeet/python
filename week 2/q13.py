# On what day of the week were you born? If you don't know the answer to this, use the calendar library to get the answer.

import datetime

# Take birth date input
year = int(input("Enter birth year (YYYY): "))
month = int(input("Enter birth month (MM): "))
day = int(input("Enter birth day (DD): "))

# Create date object
birth_date = datetime.date(year, month, day)

# Get day of the week
day_of_week = birth_date.strftime("%A")

print("You were born on a", day_of_week)
#answer enter birth year 2004
       #enter birth month 02
       #enter birth day  20
    #output You were born on Friday
