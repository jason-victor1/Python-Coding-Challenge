START

1. DEFINE FUNCTION get_sum_of_digits(num):

   - SET sum to 0
   - WHILE num > 0 DO:
     - SET last_digit to num MOD 10
     - ADD last_digit to sum
     - UPDATE num to num DIVIDED BY 10 (integer division)
   - RETURN sum

2. PROMPT the user with "Enter a number:"
3. READ user_num

4. CALL get_sum_of_digits(user_num) and STORE the result in total

5. DISPLAY "The total sum of digits is:" followed by total

END
