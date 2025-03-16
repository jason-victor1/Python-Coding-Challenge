def calculate_average():
    # Prompt the user to enter the number of elements and convert it to an integer
    num_input = int(input("Enter the number of elements: "))

    # Initialize the variable 'total' to accumulate the sum of all elements
    total = 0

    # Loop through the range equal to the number of inputs provided
    for i in range(num_input):
        # Prompt the user to enter an element and convert it to an integer
        elem = int(input("Enter the element: "))
        # Add the current element to the total sum
        total += elem

    # Check if the number of inputs is greater than zero to avoid division by zero
    if num_input > 0:
        # Calculate the average by dividing the total sum by the number of elements
        average = total / num_input
        # Print the average, formatted to two decimal places
        print(f"The average of the elements is: {average:.2f}")
    else:
        # Inform the user that no elements were entered and therefore average cannot be calculated
        print("No elements were entered. Cannot calculate average.")


# Call the function to execute the average calculation
calculate_average()
