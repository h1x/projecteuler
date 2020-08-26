# n! means n × (n − 1) × ... × 3 × 2 × 1
#
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!

def fact(number):
    if number == 1 or number == 0:
        return 1;
    else:
        return fact(number - 1) * number;

hundredFact = str(fact(100));
result = 0;

for i in range(len(hundredFact)):
    result += int(hundredFact[i]);

print(result);
