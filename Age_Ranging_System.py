from datetime import datetime

# Prompt the user for their name and age
name = input("Enter your name:")
age = int(input("Enter your age: "))

# Prompt the user for their date of birth (month, day, year)
month = int(input("Enter your birth month (MM): "))
day = int(input("Enter your birth day (DD): "))
year = int(input("Enter your birth year (YYYY): "))

# Format the date of birth
date_of_birth = datetime(year,month,day).strftime("%m-%d-%Y")

# Determine the age category
if age >= 60:
    age_category = "Senior Age Adult"
elif age >= 30:
    age_category = "Middle Age Adult"
elif age >= 18:
    age_category = "Young Adult"
elif age >= 16:
    age_category = "Teen"
elif age >= 13:
    age_category = "Pre Teen"
else:
    age_category = "Child"
    
# Print a personalized    greeting with date of birth
print(f"Hello, {name} ! You are registered as a '{age_category} ' . Your date of birth is {date_of_birth}. ")
