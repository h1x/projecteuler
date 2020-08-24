# A palindromic number reads the same both ways. The largest
# palindrome made from the product of two 2-digit numbers is
# 9009 = 91 × 99. Find the largest palindrome made from the
# product of two 3-digit numbers.

result = 0;

for i in range(999, 100, -1):
    for j in range(i, 100, -1):
        current = i * j;
        if current > result:
            numAsString = str(i * j);
            if numAsString == numAsString[::-1]:
                 result = i * j;
                 
print(result)
