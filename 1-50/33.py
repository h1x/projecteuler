# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
# attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is
# correct, is obtained by cancelling the 9s.
#
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
# There are exactly four non-trivial examples of this type of fraction, less than
# one in value, and containing two digits in the numerator and denominator.
#
# If the product of these four fractions is given in its lowest common terms,
# find the value of the denominator.

finalNum = 1;
finalDenom = 1;

def cancellingFraction(n, d):
    for i in range(2, n + 1):
        while n % i == 0 and d % i == 0:
            n /= i;
            d /= i;
    return int(n), int(d);

for numerator in range(10, 100):
    for denominator in range(10,100):
        if denominator > numerator and numerator % 10 != 0 and denominator % 10 != 0:
            cancelledN, cancelledD = cancellingFraction(numerator, denominator);
            if cancelledD < 10 and cancelledN < 10:
                cancelledSimpN = 1;
                cancelledSimpD = 1;
                if str(numerator)[0] == str(denominator)[0]:
                    cancelledSimpN, cancelledSimpD = cancellingFraction(int(str(numerator)[1]), int(str(denominator)[1]));
                elif str(numerator)[0] == str(denominator)[1]:
                    cancelledSimpN, cancelledSimpD = cancellingFraction(int(str(numerator)[1]), int(str(denominator)[0]));
                elif str(numerator)[1] == str(denominator)[0]:
                    cancelledSimpN, cancelledSimpD = cancellingFraction(int(str(numerator)[0]), int(str(denominator)[1]));
                elif str(numerator)[1] == str(denominator)[1]:
                    cancelledSimpN, cancelledSimpD = cancellingFraction(int(str(numerator)[0]), int(str(denominator)[0]));

                if cancelledN == cancelledSimpN and cancelledD == cancelledSimpD:
                    finalNum *= numerator;
                    finalDenom *= denominator;

finalNum, finalDenom = cancellingFraction(finalNum, finalDenom);

print(finalDenom);
