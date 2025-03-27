def remove_duplicate(your_str):
    # Initialize an empty string to store characters without duplicates
    result = ""
    # Iterate over each character in the input string
    for char in your_str:
        # If the character is not already in the result string, then add it
        if char not in result:
            result += char
    # Return the string that contains only unique characters
    return result


# Prompt the user to enter a string
user_input = input("What is your string?: ")

# Call the function remove_duplicate to process the input string
no_duplicate = remove_duplicate(user_input)

# Print the resulting string without duplicate characters
print(f"Without duplicate: {no_duplicate}")
