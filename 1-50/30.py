# Surprisingly there are only three numbers that can be written as the sum of 
# fourth powers of their digits:
# 
# 1634 = 1^4 + 6^4 + 3^4 + 4^4
# 8208 = 8^4 + 2^4 + 0^4 + 8^4
# 9474 = 9^4 + 4^4 + 7^4 + 4^4
# As 1 = 1^4 is not a sum it is not included.
# 
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
# 
# Find the sum of all the numbers that can be written as the sum of fifth 
# powers of their digits.

import math

result = 0;

for i in range(10, 400000):
    currentDigitSum = 0;
    currentNumber = i;

    while currentNumber != 0:
        nextDigit = currentNumber % 10;
        currentDigitSum += nextDigit**5;
        currentNumber = math.floor(currentNumber / 10);

    if currentDigitSum == i:
        #print(i);
        result += i;

print(result);
