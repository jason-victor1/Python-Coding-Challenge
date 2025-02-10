# Function to merge and sort two lists
def mergeList(first, second):
    # Combine both lists using the + operator
    combined = first + second

    # Sort the combined list in ascending order
    combined.sort()

    # Return the sorted combined list
    return combined


# Define the first list of integers
group1 = [11, 13, 18, 17, 56]

# Define the second list of integers
group2 = [12, 15, 19, 43, 66]

# Merge and sort the two lists using the mergeList function
merged = mergeList(group1, group2)

# Print the merged and sorted list
print(merged)
