# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written
# out in words, how many letters would be used?
#
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
# contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of
# "and" when writing out numbers is in compliance with British usage.

result = 0;

digits = [3, 3, 5, 4, 4, 3, 5, 5, 4];
tens = [3, 6, 6, 5, 5, 5, 7, 6, 6];
hundreds = [10, 10, 12, 11, 11, 10, 12, 12, 11];
hundredAnd = 3;
teen = [6, 6, 8, 8, 7, 7, 9, 8, 8]

for i in range(1, 1001):
    if i < 10:
        result += digits[i - 1];
    elif i == 10:
        result += tens[0];
    elif i < 20:
        result += teen[i % 10 - 1];
    elif i < 100:
        second = i % 10;
        first = (i - second) / 10;
        if second != 0:
            result += digits[int(second) - 1] + tens[int(first) - 1];
        else:
            result += tens[int(first) - 1];
    elif i < 1000:
        third = i % 10;
        second = ((i - third) / 10) % 10;
        first = ((i - 10 * second) - third) / 100;

        if second == 0 and third == 0:
            result += hundreds[int(first) - 1];
        elif second == 0 and third != 0:
                result += hundreds[int(first) - 1] + digits[int(third) - 1] + hundredAnd;
        elif second == 1 and third != 0:
            result += hundreds[int(first) - 1] + teen[int(third) - 1] + hundredAnd;
        elif second != 0 and third == 0:
            result += hundreds[int(first) - 1] + tens[int(second) - 1] + hundredAnd;
        else:
            result += hundreds[int(first) - 1] + tens[int(second) - 1] + digits[int(third) - 1] + hundredAnd;
    else:
        result += 11;

print(result);
