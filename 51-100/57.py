# It is possible to show that the square root of two can be expressed as an
# infinite continued fraction.
#
# sqrt(2) = 1 + 1 / (2 + 1 / (2 + 1 / (2 + ...)))
#
# By expanding this for the first four iterations, we get:
#
#  1 + 1/2 = 3/2 = 1.5
#  1 + 1/(2+1/2) = 7/5 = 1.4
#  1 + 1/(2+1/(2+1/2)) = 17/12 = 1.41666...
#  1 + 1/(2+1/(2+1/(2+1/2))) = 41/29 = 1.41379...
#
# The next three expansions are 90/30, 239/169, and 577/408, but the eighth expansion,
# 1393/985, is the first example where the number of digits in the numerator
# exceeds the number of digits in the denominator.
#
# In the first one-thousand expansions, how many fractions contain
# a numerator with more digits than the denominator?

def nextExpansion(n, d):
    return n + 2 * d, d + n;

n = 1;
d = 1;
count = 0;

for i in range(1000):
    n, d = nextExpansion(n, d);
    if len(str(n)) > len(str(d)):
        count += 1;

print(count);
