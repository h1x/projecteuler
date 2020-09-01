# Starting with the number 1 and moving to the right in a clockwise
# direction a 5 by 5 spiral is formed as follows:
#
#       21 22 23 24 25
#       20  7  8  9 10
#       19  6  1  2 11
#       18  5  4  3 12
#       17 16 15 14 13
#
# It can be verified that the sum of the numbers on the diagonals is 101.
#
# What is the sum of the numbers on the diagonals in a 1001 by 1001
# spiral formed in the same way?

bottomRightDiagonal = 1;
result = 1;

def calculateNextBottomRight(square):
    size = square * 2 + 1;
    return size * 4 - 2;

for fromCenter in range(500):
    bottomRightDiagonal += calculateNextBottomRight(fromCenter);
    result += 4 * bottomRightDiagonal + 12 * (fromCenter + 1);

print(result);
