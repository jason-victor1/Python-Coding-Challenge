def square_sum(num):
    # Initialize the sum to 0 to accumulate the squares of numbers
    sum = 0
    # Loop through all numbers from 0 up to and including 'num'
    for i in range(num + 1):
        # Calculate the square of the current number i
        square = i ** 2
        # Add the square to the cumulative sum
        sum = sum + square
    # Return the final sum of all squared numbers
    return sum


# Prompt the user to enter a number and convert the input to an integer
num = int(input("Enter a number: "))

# Call the square_sum function to compute the sum of squares up to 'num'
sum = square_sum(num)

# Print the resulting sum of square numbers
print("sum of square numbers is ", sum)
