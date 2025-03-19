def get_sum_of_digits(num):
    # Initialize the sum to zero to store the sum of digits
    sum = 0

    # Loop until the number becomes 0
    while (num > 0):
        # Extract the last digit of the number
        last_digit = num % 10

        # Add the last digit to the sum
        sum = sum + last_digit

        # Remove the last digit from the number by performing integer division
        num = num // 10

    # Return the sum of digits
    return sum


# Prompt the user to enter a number and convert the input to an integer
user_num = int(input("Enter a number: "))

# Call the function to calculate the sum of digits of the entered number
total = get_sum_of_digits(user_num)

# Print the total sum of digits
print(f"The total sum of digits is {total}")
