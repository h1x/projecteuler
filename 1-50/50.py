# The prime 41, can be written as the sum of six consecutive primes:
#
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
#
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
#
# Which prime, below one-million, can be written as the sum of the most consecutive primes?

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
            return False;
        elif n % (i + 2) == 0:
            return False;
        i += 6;
    return True;

result = 2;
primes = [2];
i = 3;
while result < 1000000:
    if isPrime(i) == True:
        result += i;
        primes.append(i);
    i += 2;
terms = len(primes);
found = False;

for n in range(1, terms + 1):
    if found == True:
        break;
    for front in range(n + 1):
        if found == True:
            break;
        tempResult = result;
        tempTerms = terms;
        back = n - front;

        for removeFront in range(front):
            tempTerms -= 1;
            tempResult -= primes[removeFront];
        for removeBack in range(back):
            tempTerms -= 1;
            tempResult -= primes[len(primes) - removeBack - 1];

        if isPrime(tempResult) == True:
            found = True;
            result = tempResult;
            terms = tempTerms;

print(result);
