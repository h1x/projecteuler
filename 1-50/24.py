# A permutation is an ordered arrangement of objects. For example,
# 3124 is one possible permutation of the digits 1, 2, 3 and 4. If
# all of the permutations are listed numerically or alphabetically,
# we call it lexicographic order. The lexicographic permutations of 0, 1
# and 2 are:
#
#     012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits 0, 1, 2,
# 3, 4, 5, 6, 7, 8 and 9?

import math

n = 1000000;
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"];
numberCount = len(numbers);
usedNumbers = [False] * len(numbers);

result = "";

def fact(k):
    if k <= 1:
        return 1;
    else:
        return fact(k - 1) * k;

def determineNextIndex(wantedIndex):
    for i in range(len(numbers)):
        if usedNumbers[i] == True:
            wantedIndex += 1;
        if i == wantedIndex:
            return i;

for i in range(numberCount):
    currentFact = fact(len(numbers) - i - 1);
    timesCurrentFactFitsInN = math.floor(n / currentFact);
    if ((n / currentFact) * 10) % 10 != 0:
        indexOfNextNumber = determineNextIndex(math.ceil(n / currentFact) - 1);
        n = n - currentFact * timesCurrentFactFitsInN;
    else:
        indexOfNextNumber = determineNextIndex(int(n / currentFact) - 1);
        n = n - currentFact * (timesCurrentFactFitsInN - 1);
    result += numbers[indexOfNextNumber];
    usedNumbers[indexOfNextNumber] = True;

print(result);
