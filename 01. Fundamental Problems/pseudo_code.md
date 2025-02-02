1. START

2. PRINT "Enter a year: "  // Prompt the user for input
3. INPUT year  // Read user input and store it in 'year'
4. CONVERT year TO INTEGER year_num  // Convert the input to an integer

5. IF (year_num is divisible by 4 AND NOT divisible by 100) OR (year_num is divisible by 400) THEN
      6. PRINT year_num, "is a leap year."  // If condition is met, print that it's a leap year
7. ELSE
      8. PRINT year_num, "is not a leap year."  // Otherwise, print that it's not a leap year
9. END IF

10. END