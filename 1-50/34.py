# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
# Note: As 1! = 1 and 2! = 2 are not sums they are not included.

digitFactorials = [0] * 10;
result = 0;

def fact(n):
    if n == 1 or n == 0:
        return 1;
    else:
        return fact(n - 1) * n;

for i in range(10):
    digitFactorials[i] = fact(i);

for i in range(10, 1000000):
    current = 0;
    number = i;
    while number:
        current += digitFactorials[number % 10];
        number //= 10;
    if current == i:
         print(i);
         result += i;

print(result);
