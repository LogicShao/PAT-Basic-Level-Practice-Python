n = int(input())
a = []
for _ in range(n):
    name, id, score = input().split()
    a.append((name, id, int(score)))
a.sort(key=lambda x: x[2])
print(a[-1][0], a[-1][1])
print(a[0][0], a[0][1])