from collections import Counter

m, n, Tol = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]
cnt = Counter([g[x][y] for x in range(n) for y in range(m)])
res = []
for i in range(n):
    for j in range(m):
        if cnt[g[i][j]] > 1:
            continue
        tocmp = [g[x][y] for x in range(
            i - 1, i + 2) for y in range(j - 1, j + 2)
            if 0 <= x < n and 0 <= y < m and (x != i or y != j)]
        if all(abs(g[i][j] - x) > Tol for x in tocmp):
            res.append((i + 1, j + 1))
if len(res) == 0:
    print('Not Exist')
elif len(res) == 1:
    x, y = res[0]
    print('({}, {}): {}'.format(y, x, g[x - 1][y - 1]))
else:
    print('Not Unique')
