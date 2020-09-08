# In the United Kingdom the currency is made up of pound (£) and pence (p).
# There are eight coins in general circulation:
#
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
# It is possible to make £2 in the following way:
#
# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?

coins = [1, 2, 5, 10, 20, 50, 100, 200];
finalValue = 200;

# Every value represents the number of different ways that are possible to make a value equal to the index
# In our case, we'll need result[200] 
result = [1] + [0] * finalValue;

for coin in coins:
    for i in range(coin, finalValue + 1):
        result[i] += result[i - coin]

print(result[finalValue]);
