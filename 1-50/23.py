# A perfect number is a number for which the sum of its proper divisors is
# exactly equal to the number. For example, the sum of the proper divisors of
# 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less than
# n and it is called abundant if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
# number that can be written as the sum of two abundant numbers is 24. By
# mathematical analysis, it can be shown that all integers greater than 28123
# can be written as the sum of two abundant numbers. However, this upper limit
# cannot be reduced any further by analysis even though it is known that the
# greatest number that cannot be expressed as the sum of two abundant numbers is
# less than this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum
# of two abundant numbers.

sum = 0;

abundantNumbers = [];
canItBeWritten = [False] * 28123;

def isItAbundant(number):
    divisorSum = 0
    for i in range(1, int(number / 2) + 1):
        if number % i == 0:
            divisorSum += i;
    if number < divisorSum:
        return True;
    else:
        return False;

def updateList():
    for i in range(len(abundantNumbers)):
        if abundantNumbers[i] + abundantNumbers[len(abundantNumbers) - 1] - 1 < len(canItBeWritten):
            canItBeWritten[abundantNumbers[i] + abundantNumbers[len(abundantNumbers) - 1] - 1] = True;

for i in range(1, 28123):
    if isItAbundant(i):
        abundantNumbers.append(i);
        updateList();
    if canItBeWritten[i - 1] == False:
        sum += i;


print(sum);
