# This script counts the number of words in a given text.
# It does so by counting the number of spaces and then adding one,
# since the number of words is always one more than the number of spaces.

# Define the text string to be processed.
text = "I'm learning Python right now"

# Initialize a counter to count the number of spaces in the text.
count = 0

# Iterate over each character in the text.
for char in text:
    # If the character is a space, increment the counter.
    if char == " ":
        count += 1

# Since there is one more word than the number of spaces,
# add 1 to the count to get the total number of words.
count += 1

# Print the final word count.
print(count)
