# A googol (10^100) is a massive number: one followed by one-hundred zeros;
# 100^100 is almost unimaginably large: one followed by two-hundred zeros.
# Despite their size, the sum of the digits in each number is only 1.
#
# Considering natural numbers of the form, a^b, where a, b < 100,
# what is the maximum digital sum?

result = 0;

def digitSum(n):
    result = 0;
    strN = str(n);
    for i in range(len(strN)):
        result += int(strN[i]);
    return result;

for a in range(1, 100):
    for b in range(1, 100):
        current = digitSum(a ** b);
        if result < current:
            result = current

print(result);
