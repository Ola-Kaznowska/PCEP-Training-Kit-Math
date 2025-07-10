# Read initial account balance, interest rate, and years from user
initial_balance = float(input("Enter initial account balance: "))
rate = float(input("Enter annual interest rate (in %): "))
years = int(input("Enter number of years: "))

# Calculate final balance using compound interest formula
final_balance = initial_balance * (1 + rate / 100) ** years

# Display result rounded to two decimal places
print(f"Account balance after {years} years: {final_balance:.2f}")