# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of
# each of the digits 0 to 9 in some order, but it also has a rather interesting
# sub-string divisibility property.
#
# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note
# the following:
#
#   d2d3d4=406 is divisible by 2
#   d3d4d5=063 is divisible by 3
#   d4d5d6=635 is divisible by 5
#   d5d6d7=357 is divisible by 7
#   d6d7d8=572 is divisible by 11
#   d7d8d9=728 is divisible by 13
#   d8d9d10=289 is divisible by 17
#
# Find the sum of all 0 to 9 pandigital numbers with this property.

from itertools import permutations

numbers = list(permutations("0123456789"));
listLen = len(numbers);
result = 0;

def firstRule(n):
    if int(n / 1000000) % 2 == 0:
        return True;
    return False;
def secondRule(n):
    if int((n % 100000000) / 100000) % 3 == 0:
        return True;
    return False;
def thirdRule(n):
    if int(n / 10000) % 5 == 0:
        return True;
    return False;
def fourthRule(n):
    if int((n % 1000000) / 1000) % 7 == 0:
        return True;
    return False;
def fifthRule(n):
    if int((n % 100000) / 100) % 11 == 0:
        return True;
    return False;
def sixthRule(n):
    if int((n % 10000) / 10) % 13 == 0:
        return True;
    return False;
def seventhRule(n):
    if (n % 1000) % 17 == 0:
        return True;
    return False;

for i in range(int(listLen / 10), listLen):
    if firstRule(int(''.join(numbers[i]))) == True:
        if thirdRule(int(''.join(numbers[i]))) == True:
            if seventhRule(int(''.join(numbers[i]))) == True:
                if secondRule(int(''.join(numbers[i]))) == True:
                    if fourthRule(int(''.join(numbers[i]))) == True:
                        if fifthRule(int(''.join(numbers[i]))) == True:
                            if sixthRule(int(''.join(numbers[i]))) == True:
                                result += int(''.join(numbers[i]));
print(result)
