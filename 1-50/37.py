# The number 3797 has an interesting property. Being prime itself,
# it is possible to continuously remove digits from left to right, and
# remain prime at each stage: 3797, 797, 97, and 7. Similarly we can
# work from right to left: 3797, 379, 37, and 3.
#
# Find the sum of the only eleven primes that are both truncatable
# from left to right and right to left.
#
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

import math

sum = 0;
truncatableCount = 0;

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

number = 11;
while truncatableCount < 11:
    if '4' not in str(number) and '6' not in str(number) and '8' not in str(number) and str(number)[0] != '1' and str(number)[len(str(number)) - 1] != '1' and str(number)[0] != '9' and str(number)[len(str(number)) - 1] != '9':
        if isPrime(number) == True:
            digitTracker = 10 ** (len(str(number)) - 1);
            normalR = int(number / 10);
            normalL = number % digitTracker;
            digitTracker = int(digitTracker / 10);
            isTruncatable = True;
            while normalR > 0:
                if isPrime(normalR) == False or isPrime(normalL) == False:
                    isTruncatable = False;
                    break;
                else:
                    normalR = int(normalR / 10);
                    normalL = normalL % digitTracker;
                    digitTracker = int(digitTracker / 10);
            if isTruncatable == True:
                sum += number;
                truncatableCount += 1;
    number += 2;

print(sum);
