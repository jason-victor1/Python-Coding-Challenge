def count_vowels(sentence):
    # Define a string containing all vowel characters (both uppercase and lowercase)
    vowels = "aeiouAEIOU"

    # Initialize a counter to keep track of the number of vowels
    count = 0

    # Iterate through each character in the given sentence
    for char in sentence:
        # Check if the character is a vowel
        if char in vowels:
            # Increment the count if it is a vowel
            count += 1

    # Return the total count of vowels in the sentence
    return count


# Test the function with a sample sentence and print the result
print(count_vowels("I'm learning Python right now"))
