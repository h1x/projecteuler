# Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:
#
# Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
# Pentagonal	 	Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
# Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
# It can be verified that T285 = P165 = H143 = 40755.
#
# Find the next triangle number that is also pentagonal and hexagonal.

def isPentagonal(n):
    num = ((24 * n + 1)**0.5 + 1) / 6;
    return num == int(num);

found = False;
result = 0;
i = 144;

while found == False:
    hex = int(i*(2*i-1));
    if isPentagonal(hex) == True:
        result = hex;
        found = True;
    i += 1;

print(result);
