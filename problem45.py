# Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:
# Triangle	T_n=n(n+1)/2	1, 3, 6, 10, 15, ...
# Pentagonal	P_n=n(3n-1)/2	1, 5, 12, 22, 35, ...
# Hexagonal	H_n=n(2n-1)	1, 6, 15, 28, 45, ...
# It can be verified that T_285 = P_165 = H_143 = 40755.
# Find the next triangle number that is also pentagonal and hexagonal.

from math import sqrt, floor

def isPentagonal(x):
	n = (sqrt(24 * x + 1) + 1) / 6
	return n - floor(n) == 0

def isHexagonal(x):
	n = (sqrt(8 * x + 1) + 1) / 4
	return n - floor(n) == 0

for n in range(286, 1000000):
	x = int(n * (n + 1) / 2)
	if isPentagonal(x) and isHexagonal(x):
		print(x)
		break
