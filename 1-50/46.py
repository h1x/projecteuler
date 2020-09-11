# It was proposed by Christian Goldbach that every odd composite number can be
# written as the sum of a prime and twice a square.
#
# 9 = 7 + 2×1^2
# 15 = 7 + 2×2^2
# 21 = 3 + 2×3^2
# 25 = 7 + 2×3^2
# 27 = 19 + 2×2^2
# 33 = 31 + 2×1^2
#
# It turns out that the conjecture was false.
#
# What is the smallest odd composite that cannot be written as the sum of a prime
# and twice a square?

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


found = False;
result = 0;
n = 9;

while found == False:
    currentFound = False;
    if isPrime(n) == False:
        for i in range(2, n - 1):
            if isPrime(i) == True:
                square = int((n - i) / 2);
                if int(square ** 0.5) == square ** 0.5:
                    currentFound = True;
                    break;
        if currentFound == False:
            result = n;
            found = True;
            break;
    n += 2;

print(result);
