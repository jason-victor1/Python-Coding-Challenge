def get_sum(nums):
    # Initialize the variable 'sum' to 0 to store the cumulative sum of the list elements
    sum = 0
    # Loop through each number in the list 'nums'
    for num in nums:
        # Add the current number to the cumulative sum
        sum = sum + num
    # Return the final sum after processing all elements in the list
    return sum


# Define a list of numbers
nums = [13, 89, 65, 42, 12, 11, 56]

# Call the get_sum function with the list 'nums' and store the result in 'total'
total = get_sum(nums)
# Print the total sum of all elements in the list
print(f"The total of each elements {total}")
