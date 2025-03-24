START

1. DEFINE FUNCTION square_sum(num):

   - SET sum to 0 // Initialize the sum to accumulate the squares
   - FOR i FROM 0 TO num DO:
     - SET square to i raised to the power of 2 // Calculate the square of i
     - ADD square to sum // Update the cumulative sum with the current square
   - END FOR
   - RETURN sum // Return the final sum of squares

2. PROMPT the user with "Enter a number:"
3. READ num // Convert the input to an integer

4. CALL square_sum(num) and STORE the result in sum

5. DISPLAY "sum of square numbers is " followed by sum

END
