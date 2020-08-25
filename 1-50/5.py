# 2520 is the smallest number that can be divided by each
# of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly
# divisible by all of the numbers from 1 to 20?

import math

result = 1;

for i in range(2, 21):
    gcd = math.gcd(result, i);
    temp = i / gcd;
    result *= int(temp);

print(result);
