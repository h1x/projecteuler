# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 21000?


digits = str(pow(2, 1000));
result = 0;

for i in range(len(digits)):
    result += int(digits[i]);

print(result);
