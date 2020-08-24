# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

num = 600851475143;
prime = 2;
biggest = -1;

while num >= prime^2:
    if(num % prime == 0):
        biggest = prime;
        num /= prime;
    else:
        prime += 1;

if num > prime:
    print(num);
else:
    print(biggest);
