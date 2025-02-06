1. START

2. DEFINE FUNCTION remove_duplicate(items)
      1. SET unique_list TO empty list  // Initialize an empty list to hold unique items

      2. FOR each item IN items DO
            1. IF item IS NOT IN unique_list THEN
                  1. ADD item TO unique_list  // Add the item if it's not already in the unique_list
            2. END IF
      3. END FOR

      4. RETURN unique_list  // Return the list of unique items
3. END FUNCTION

4. SET numbers TO [22, 11, 3, 1, 4, 5, 5, 2, 2, 11, 66, 89]  // Define a list with duplicate numbers

5. PRINT remove_duplicate(numbers)  // Call the function and print the result

6. END
