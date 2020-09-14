# By replacing the 1st digit of the 2-digit number *3, it turns out that
# six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
#
# By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit
# number is the first example having seven primes among the ten generated numbers,
#  yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993.
#  Consequently 56003, being the first member of this family, is the smallest
#  prime with this property.
#
# Find the smallest prime which, by replacing part of the number (not necessarily
# adjacent digits) with the same digit, is part of an eight prime value family.

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

result = 0;
found = False;
i = 11;

while found == False:
    if isPrime(i) == True:
        currentNum = str(i);
        for digit in range(10):
            if str(digit) in currentNum[:len(currentNum) - 1]:
                currentCount = 0;
                notPrime = 0;
                for replace in range(10):
                    newNum = "";
                    for n in range(len(currentNum) - 1):
                        if currentNum[n] == str(digit):
                            newNum += str(replace);
                        else:
                            newNum += currentNum[n];
                    newNum += currentNum[len(currentNum) - 1];
                    if newNum[0] != '0' and isPrime(int(newNum)) == True:
                        currentCount += 1;
                    else:
                        notPrime += 1;
                    if notPrime > 2:
                        break;
                if currentCount == 8:
                    result = i;
                    found = True;
                    break;
    i += 2;

print(result);
