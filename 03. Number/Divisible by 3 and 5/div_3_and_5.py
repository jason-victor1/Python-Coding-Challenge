def divisible_by_3and5(num):
    # Initialize an empty list to store numbers that are divisible by both 3 and 5
    result = []

    # Loop through all numbers from 0 up to (but not including) 'num'
    for i in range(num):
        # Check if the current number is divisible by both 3 and 5
        if i % 3 == 0 and i % 5 == 0:
            # If true, add the number to the result list
            result.append(i)

    # Return the list of numbers that meet the criteria
    return result


# Prompt the user to enter a number and convert the input to an integer
num = int(input("Enter your number: "))
# Call the function with the user input and store the returned list in 'result'
result = divisible_by_3and5(num)
# Print the list of numbers that are divisible by both 3 and 5
print(result)
