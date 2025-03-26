START

1. DEFINE FUNCTION get_second_smallest(nums):

   - SET smallest to the first element of nums
   - SET second_smallest to the first element of nums
   - FOR each index i from 1 to (length of nums - 1) DO:
     - IF nums[i] is less than smallest THEN:
       - SET second_smallest to smallest
       - SET smallest to nums[i]
     - ELSE IF nums[i] is less than second_smallest THEN:
       - SET second_smallest to nums[i]
   - RETURN second_smallest

2. SET my_nums to the list [44, 11, 83, 29, 25, 76, 88]

3. CALL get_second_smallest(my_nums) and STORE the result in second_smallest

4. DISPLAY "Second smallest number is " followed by second_smallest

END
