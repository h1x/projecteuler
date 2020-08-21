# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

sum = 0;
sieveOfEratosthenes = [True] * 2000000;

for p in range(2, 2000000):
    if sieveOfEratosthenes[p]:
        sum += p
        for i in range(p*p, 2000000, p):
            sieveOfEratosthenes[i] = False

print(sum);
