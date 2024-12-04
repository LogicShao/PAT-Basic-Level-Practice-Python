n, t = map(int, input().split())
a = list(map(int, input().split()))
res = []
i = 0
while i < n:
    j = i
    while j < n and a[j] > t:
        j += 1
    if j > i:
        res.append((i, j - 1))
    i = j + 1
for l, r in res:
    print('[{}, {}]'.format(l, r))
if not res:
    print(max(a))
