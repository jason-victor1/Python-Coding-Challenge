def get_largest(nums):
    # Initialize 'largest' with the first element of the list
    largest = nums[0]

    # Loop through each number in the list
    for num in nums:
        # If the current number is greater than the current largest, update largest
        if num > largest:
            largest = num

    # Return the largest number found in the list
    return largest


# Define a list of numbers
my_nums = [0, 15, 68, 1, 0, -55]

# Call the function get_largest with the list and store the result in 'largest'
largest = get_largest(my_nums)

# Print the largest number from the list
print(f"The largest number is {largest}")
