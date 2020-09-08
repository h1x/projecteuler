# We shall say that an n-digit number is pandigital if it makes use of all the
# digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through
# 5 pandigital.
#
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
# multiplicand, multiplier, and product is 1 through 9 pandigital.
#
# Find the sum of all products whose multiplicand/multiplier/product identity
# can be written as a 1 through 9 pandigital.
#
# HINT: Some products can be obtained in more than one way so be sure to only
# include it once in your sum.

sum = 0;

for n in range(1100, 10000):
    if str(n)[0] == str(n)[1] or str(n)[0] == str(n)[2] or str(n)[0] == str(n)[3] or str(n)[1] == str(n)[2] or str(n)[1] == str(n)[3] or str(n)[2] == str(n)[3]:
        pass;
    else:
        for multiplicand in range(2, 100):
            if n % multiplicand == 0:
                multiplier = int(n / multiplicand);
                if len(str(n) + str(multiplicand) + str(multiplier)) == 9 and '0' not in str(multiplier) and '0' not in str(multiplicand) and '0' not in str(n):
                    combined = str(multiplier) + str(multiplicand) + str(n);
                    isUsed = [False] * 9;
                    pandigital = True;

                    for i in range(9):
                        if isUsed[int(combined[i]) - 1] == True:
                            pandigital = False;
                            break;
                        else:
                            isUsed[int(combined[i]) - 1] = True;

                    if pandigital == True:
                        sum += n;
                        break;

print(sum);
