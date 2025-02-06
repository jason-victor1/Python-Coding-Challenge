# Define a function to remove duplicate items from a list
def remove_duplicate(items):
    # Initialize an empty list to store unique items
    unique = []

    # Loop through each item in the provided list
    for item in items:
        # Check if the current item is not already in the unique list
        if item not in unique:
            # If the item is unique, add it to the unique list
            unique.append(item)

    # Return the list containing only unique items
    return unique


# Define a list containing some duplicate numbers
numbers = [22, 11, 3, 1, 4, 5, 5, 2, 2, 11, 66, 89]

# Call the remove_duplicate function and print the result
print(remove_duplicate(numbers))
