n = int(input())
data = []
for i in range(n):
    Id, x, y = input().split()
    data.append((Id, int(x), int(y)))
mx = max(data, key=lambda x: x[1]**2 + x[2]**2)[0]
mn = min(data, key=lambda x: x[1]**2 + x[2]**2)[0]
print(mn, mx)