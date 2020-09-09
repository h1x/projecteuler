# The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.
#
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
#
# (Please note that the palindromic number, in either base, may not include leading zeros.)

sum = 0;

def isPalindromic(number):
    for i in range(len(number)):
        if number[i] != number[len(str(number)) - i - 1]:
            return False;
    return True;


for n in range(1, 1000000, 2):
    if isPalindromic(str(n)) == True:
        temp = bin(n)[2:];
        if isPalindromic(temp) == True:
            sum += n;

print(sum);
