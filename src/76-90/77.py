EPS = 1e-9
n, m = map(int, input().split())
for i in range(n):
    data = list(filter(lambda x: 0 <= x <= m, map(int, input().split())))
    G1 = data[0]
    d2 = data[1:]
    G2 = (sum(d2) - max(d2) - min(d2)) / (len(d2) - 2)
    print(round((G1 + G2 + EPS) / 2))
