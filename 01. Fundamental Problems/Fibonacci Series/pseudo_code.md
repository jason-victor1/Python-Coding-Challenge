1. **START**

2. **DEFINE FUNCTION** `fibonacci(num)`
   1. **SET** `fibo` **TO** `[0, 1]`  // Initialize list with the first two Fibonacci numbers
   2. **SET** `i` **TO** `2`  // Starting index for iteration

   3. **WHILE** `i` **IS LESS THAN OR EQUAL TO** `num` **DO**
      1. **SET** `next_fibo` **TO** `fibo[i-1] + fibo[i-2]`  // Compute next Fibonacci number
      2. **APPEND** `next_fibo` **TO** `fibo`  // Add the computed number to the list
      3. **INCREMENT** `i` **BY** `1`  // Move to the next index
   4. **END WHILE**

   5. **RETURN** `fibo`  // Return the complete Fibonacci sequence

3. **END FUNCTION**

4. **PRINT** `fibonacci(9)`  // Call the function with 9 and print the result

5. **END**