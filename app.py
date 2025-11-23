print("Welcome to my Python program!")

hours = input("How many hours did you work this week? ")
pay = input("What is your hourly pay rate? ")
hours = float(hours)
pay = float(pay)

monthly_pay = hours * 4 * pay

print(f"Your estimated monthly pay is: ${monthly_pay:.2f}")