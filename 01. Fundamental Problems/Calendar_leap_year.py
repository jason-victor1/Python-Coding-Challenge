# Prompt the user to enter a year
year = input("Enter a year: ")

# Convert the input string to an integer
year_num = int(year)

# Check for leap year using the correct rules:
# 1. A year is a leap year if it is divisible by 4.
# 2. However, if the year is also divisible by 100, it is NOT a leap year.
# 3. But if the year is divisible by 400, then it IS a leap year.
if (year_num % 4 == 0 and year_num % 100 != 0) or (year_num % 400 == 0):
    # If the year meets the conditions above, it is a leap year.
    print(year_num, "is a leap year.")
else:
    # If the conditions are not met, it is not a leap year.
    print(year_num, "is not a leap year.")
