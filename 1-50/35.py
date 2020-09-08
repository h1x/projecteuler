# The number, 197, is called a circular prime because all rotations of the
# digits: 197, 971, and 719, are themselves prime.
#
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71,
# 73, 79, and 97.
#
# How many circular primes are there below one million?

import math

count = 5;
usedPrimes = [False] * 1000000;

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

for number in range(13, 1000000, 2):
    if '5' not in str(number) and '0' not in str(number) and '2' not in str(number) and '4' not in str(number) and '6' not in str(number) and '8' not in str(number):
        if usedPrimes[number - 1] == False:
            if isPrime(number) == True:
                numberString = str(number);
                isCircular = True;
                for j in range(1, len(numberString)):
                    usedPrimes[int(numberString[-j:] + numberString[:-j]) - 1] = True;
                    if isPrime(int(numberString[-j:] + numberString[:-j])) == False:
                        isCircular = False;
                if isCircular == True:
                    count += len(numberString);

print(count);
