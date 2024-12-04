n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
mx = list(map(max, data))
print(*mx)
print(max(mx))
