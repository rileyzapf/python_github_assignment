print("Welcome to my Python program!")

hours = input("How many hours did you work this week? ") # Getting input for number of hours worked
pay = input("What is your hourly pay rate? ") # Getting input for hourly pay rate
hours = float(hours) # Turns input into a float
pay = float(pay) # Turns input into a float

monthly_pay = hours * 4 * pay # Multiplies hours by 4 weeks and pay rate to get monthly pay

print(f"Your estimated monthly pay is: ${monthly_pay:.2f}") 

try:
    hours = float(hours)
    pay = float(pay)
except ValueError:
    print("Please enter valid numbers for hours and pay rate.") # Error handling
    exit()
