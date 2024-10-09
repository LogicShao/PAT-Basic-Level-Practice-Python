import decimal

n = int(input())
a = list(map(decimal.Decimal, input().split()))
res = decimal.Decimal(0)
for i in range(n):
    x = i
    y = n - i - 1
    res += a[i] * (x * y + n)
print("{:.2f}".format(res))
