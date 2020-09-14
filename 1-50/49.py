# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases
# by 3330, is unusual in two ways: (i) each of the three terms are prime, and,
# (ii) each of the 4-digit numbers are permutations of one another.
#
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
# exhibiting this property, but there is one other 4-digit increasing sequence.
#
# What 12-digit number do you form by concatenating the three terms in this sequence?

def isPrime(n):
    if n == 2 or n == 3:
        return True;
    elif n < 2 or n % 2 == 0:
        return False;
    elif n < 9:
        return True;
    if n % 3 == 0:
        return False;

    root = int(n**0.5);
    i = 5

    while i <= root:
        if n % i == 0:
            return False
        elif n % (i + 2) == 0:
            return False;
        i += 6;
    return True;

result = "";

for i in range(1000, 10000):
    if isPrime(i) == True and i != 1487:
        if isPrime(i + 3330) == True and isPrime(i + 6660) == True:
            if sorted(str(i)) == sorted(str(i + 3330)) and sorted(str(i)) == sorted(str(i + 6660)):
                result += str(i) + str(i + 3330) + str(i + 6660);
                break;
                
print(result);
