from fractions import Fraction
from math import gcd

a, b, k = input().split()
a, b, k = Fraction(a), Fraction(b), int(k)
if a > b:
    a, b = b, a
res = []
for i in range((a.numerator * k + a.denominator - 1) // a.denominator, b.numerator * k // b.denominator + 1):
    if gcd(i, k) != 1:
        continue
    x = Fraction(i, k)
    if a < x < b:
        res.append(x)
print(*res)
