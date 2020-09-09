# If p is the perimeter of a right angle triangle with integral length sides,
# {a,b,c}, there are exactly three solutions for p = 120.
#
# {20,48,52}, {24,45,51}, {30,40,50}
#
# For which value of p ≤ 1000, is the number of solutions maximised?

import math

currentMax = -1;
currentMaxP = -1;
solutions = [0] * 1000;

for a in range(1, 501):
    for b in range(1, 501):
        c = (a * a + b * b) ** 0.5;
        if a + b + c <= 1000 and c == int(c) and a < b and b <= c:
            solutions[a + b + int(c) - 1] += 1;

for i in range(1000):
    if solutions[i] > currentMax:
        currentMax = solutions[i];
        currentMaxP = i + 1;

print(currentMaxP);
print(currentMax);
