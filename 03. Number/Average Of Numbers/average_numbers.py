# Prompt the user to enter the number of elements they want to input
num_input = int(input("How many numbers do you want to enter?: "))

# Initialize a variable to store the sum of the numbers
total = 0

# Loop through the range from 0 to num_input, prompting the user for input each time
for i in range(0, num_input):
    # Get a number from the user and convert it to an integer
    elem = int(input("Enter element: "))

    # Add the entered number to the total sum
    total += elem

# Calculate the average by dividing the total sum by the number of inputs
avg = total / num_input

# Print the average, rounded to 2 decimal places for better readability
print("Average of elements you have entered: ", round(avg, 2))
