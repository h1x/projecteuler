# The first two consecutive numbers to have two distinct prime factors are:
#
# 14 = 2 × 7
# 15 = 3 × 5
#
# The first three consecutive numbers to have three distinct prime factors are:
#
# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.
#
# Find the first four consecutive integers to have four distinct prime factors each.
# What is the first of these numbers?

def primeFactorCounter(n):
    i = 2;
    factors = [];
    while i * i <= n:
        if n % i != 0:
            i += 1;
        else:
            n //= i;
            if i not in factors:
                factors.append(i);
    if n > 1:
        factors.append(n);
    return len(factors);

result = 0;
i = 210;

while True:
    if primeFactorCounter(i) == 4:
        if primeFactorCounter(i + 1) == 4 and primeFactorCounter(i + 2) == 4 and primeFactorCounter(i + 3) == 4:
            result = i;
            break;
    i += 1;

print(result);
