a = list(map(int, input().split()))
res = []
for t, n in zip(a[::2], a[1::2]):
    if n != 0:
        res.append(t * n)
        res.append(n - 1)
print(*(res or [0, 0]))
