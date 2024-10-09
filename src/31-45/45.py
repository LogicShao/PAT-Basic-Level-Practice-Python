n = int(input())
a = list(map(int, input().split()))
l = [0 for _ in range(n)]
r = [0 for _ in range(n)]
l[0] = a[0]
r[n - 1] = a[n - 1]
for i in range(1, n):
    l[i] = max(l[i - 1], a[i])
for i in range(n - 2, -1, -1):
    r[i] = min(r[i + 1], a[i])
res = []
for i in range(n):
    if i == 0:
        if a[i] <= r[i + 1]:
            res.append(a[i])
    elif i == n - 1:
        if a[i] >= l[i - 1]:
            res.append(a[i])
    else:
        if a[i] >= l[i - 1] and a[i] <= r[i + 1]:
            res.append(a[i])
print(len(res))
print(*res)
