def get_second_smallest(nums):
    # Initialize 'smallest' with the first element of the list
    smallest = nums[0]
    # Initialize 'second_smallest' with the first element of the list as well
    second_smallest = nums[0]

    # Loop through the list starting from the second element
    for i in range(1, len(nums)):
        # If the current element is less than the current smallest,
        # update second_smallest to the current smallest and smallest to the current element
        if nums[i] < smallest:
            second_smallest = smallest
            smallest = nums[i]
        # If the current element is not less than smallest but is less than second_smallest,
        # update second_smallest to the current element
        elif nums[i] < second_smallest:
            second_smallest = nums[i]

    # Return the second smallest number found in the list
    return second_smallest


# Define a list of numbers
my_nums = [44, 11, 83, 29, 25, 76, 88]

# Call the function to get the second smallest number from the list
second_smallest = get_second_smallest(my_nums)

# Print the result, displaying the second smallest number
print(f"Second smallest number is {second_smallest}")
