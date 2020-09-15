# It can be seen that the number, 125874, and its double, 251748, contain
# exactly the same digits, but in a different order.
#
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
# contain the same digits.

result = 0;
i = 1;

while True:
    current = sorted(str(i));

    if current == sorted(str(i * 2)) and current == sorted(str(i * 3)) and current == sorted(str(i * 4)) and current == sorted(str(i * 5)) and current == sorted(str(i * 6)):
        result = i;
        break;
    i += 1;

print(result);
