# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
# see that the 6th prime is 13. What is the 10 001st prime number?

import math

count = 1;
num = 1;

while count < 10001:
    num += 2;
    prime = True
    for i in range(2, int(math.sqrt(num))+1):
        if (num % i == 0):
            prime = False
    if prime:
        count += 1;

print(num);
