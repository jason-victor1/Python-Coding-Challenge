1. START  
2. SET text = "I'm learning Python right now"  // Define the text string  
3. SET count = 0  // Initialize the space counter  

4. FOR each character in text DO  // Loop through every character in the text  
  1. IF character is equal to " " THEN  // Check if the current character is a space  
    1. INCREMENT count by 1  // Increase the counter when a space is found  
  2. END IF  
5. END FOR  

6. INCREMENT count by 1  // Add one to count to include the last word  
7.  PRINT count  // Output the total number of words  
8.  END