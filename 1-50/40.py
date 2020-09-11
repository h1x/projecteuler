# An irrational decimal fraction is created by concatenating the positive integers:
#
# 0.12345678910[1]112131415161718192021...
#
# It can be seen that the 12th digit of the fractional part is 1.
#
# If dn represents the nth digit of the fractional part, find the value of the following expression.
#
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

import math

digit = 9;
result = 1;
digitSets = 2;
digitSetNumberCount = 90;
nextMilestone = 100;

while nextMilestone < 1000001:
    if digitSets * digitSetNumberCount + digit < nextMilestone:
        digit += digitSets * digitSetNumberCount;
        digitSets += 1;
        digitSetNumberCount *= 10;
    elif digitSets * digitSetNumberCount + digit >= nextMilestone:
        digit += digitSets * digitSetNumberCount;

        wantedNumberIndex = digitSetNumberCount - math.floor((digit - nextMilestone) / digitSets);
        wantedDigit = (digitSets * digitSetNumberCount - digit + nextMilestone) % digitSets;
        wantedNumber = 10 ** (digitSets - 1) + wantedNumberIndex - 1;
        #print(str(wantedNumber) + " " + str(wantedDigit) + " " + str(int(wantedNumber / (10 ** (digitSets - wantedDigit))) % 10));
        result *= int((wantedNumber / (10 ** (digitSets - wantedDigit)))) % 10;

        nextMilestone *= 10;
        digitSets += 1;
        digitSetNumberCount *= 10;


print(result);
