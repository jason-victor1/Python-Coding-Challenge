# Function to print the multiplication table for a given number 'n'
def multiplication_table(n):
    # Initialize the counter variable 'i' to 1
    i = 1

    # Use a while loop to generate the multiplication table from 1 to 10
    while i <= 10:
        # Print the current multiplication result in the format: i X n = (i * n)
        print(i, 'X', n, '=', i * n)

        # Increment the counter variable by 1 for the next iteration
        i += 1


# Call the function to print the multiplication table for 5
multiplication_table(5)
