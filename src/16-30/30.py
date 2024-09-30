import bisect

n, p = map(int, input().split())
a = sorted(map(int, input().split()))
res = 0
for i in range(n):
    res = max(res, bisect.bisect_right(a, a[i] * p) - i)
print(res)
