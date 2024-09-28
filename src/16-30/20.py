n, d = map(int, input().split())
data = sorted(list(zip(*(map(float, input().split())
                         for _ in range(2)))), key=lambda x: x[1]/x[0], reverse=True)
total, i = 0, 0
while i < n and d > 0:
    if d >= data[i][0]:
        total += data[i][1]
        d -= data[i][0]
    else:
        total += data[i][1] * d / data[i][0]
        d = 0
    i += 1
print(f'{total:.2f}')
