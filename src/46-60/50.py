N = int(input())
a = sorted(map(int, input().split()), reverse=True)
sqrtN = int(N ** 0.5)
while N % sqrtN != 0:
    sqrtN -= 1
n, m = sqrtN, N // sqrtN
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
res = [[0 for _ in range(n)] for _ in range(m)]
x, y = 0, 0
d = 0
for i in range(N):
    res[x][y] = a[i]
    nx, ny = x + direction[d][0], y + direction[d][1]
    if nx < 0 or nx >= m or ny < 0 or ny >= n or res[nx][ny] != 0:
        d = (d + 1) % 4
        nx, ny = x + direction[d][0], y + direction[d][1]
    x, y = nx, ny
for line in res:
    print(*line)
