# Euler discovered the remarkable quadratic formula:
#
#           n^2 + n + 41
#
# It turns out that the formula will produce 40 primes for the consecutive integer
# values 0 <= n <= 39. However, when n = 30, 40^2 + 40 + 41 = 40(40 + 1) + 41
# is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly
 # divisible by 41.
#
# The incredible formula n^2 - 79n + 1601 was discovered, which produces 80 primes
# for the consecutive values 0 <= n <= 79. The product of the coefficients, −79
# and 1601, is −126479.
#
# Considering quadratics of the form:
#
#           n^2 + an + b, where |a| < 1000 and |b| <= 1000
#
# where |n| is the modulus/absolute value of n
# e.g. |11| = 11 and |-4| = 4
#
# Find the product of the coefficients, a and b, for the quadratic expression
# that produces the maximum number of primes for consecutive values of n,
# starting with n = 0.

import math

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

maxN = 0;
maxProduct = 0;

for a in range(-999, 1000):
    for b in range(2, 1001):
        currentN = 0;
        while isPrime(currentN * currentN + a * currentN + b):
            currentN += 1;
        if currentN > maxN:
            maxN = currentN;
            maxProduct = a * b;

print(maxN);
print(maxProduct);
