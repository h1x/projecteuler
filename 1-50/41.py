# We shall say that an n-digit number is pandigital if it makes use of all the
# digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
#
# What is the largest n-digit pandigital prime that exists?

import math
from itertools import permutations

def isPrime(n):
    if n == 2 or n == 3:
        return True;
    elif n < 2 or n % 2 == 0:
        return False;
    elif n < 9:
        return True;
    if n % 3 == 0:
        return False;

    root = int(math.sqrt(n));
    i = 5

    while i <= root:
        if n % i == 0:
            return False
        elif n % (i + 2) == 0:
            return False;
        i += 6;
    return True;

#if n = 8 or or n = 9, all the numbers can be divided by 3, so the biggest n-digit pandigital prime is for n = 7

numbers = list(permutations("1234567"));
listLen = len(numbers);
result = 0;

for i in range(listLen):
    if int(numbers[listLen - i - 1][6]) % 2 != 0 and numbers[listLen - i - 1][6] != '5' and isPrime(int(''.join(numbers[listLen - i - 1]))) == True:
        result = int(''.join(numbers[listLen - i - 1]));
        break;

print(result);
