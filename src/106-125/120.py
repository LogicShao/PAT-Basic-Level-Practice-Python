n, m = map(int, input().split())
a = [0] + list(map(int, input().split()))
b = [0]
for i in range(1, n + 1):
    b.append(b[i - 1] + a[i])
res = 0
for i in range(1, n + 1):
    if a[i] > m:
        continue
    l, r = i, n
    while l < r:
        mid = (l + r + 1) // 2
        if b[mid] - b[i - 1] <= m:
            l = mid
        else:
            r = mid - 1
    res += l - i + 1
print(res)
