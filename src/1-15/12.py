a = list(map(int, input().split()))[1::]
a = [list(filter(lambda x: x % 5 == i, a)) for i in range(5)]
res = []
a[0] = list(filter(lambda x: x % 2 == 0, a[0]))
res.append(sum(a[0]) if a[0] else 'N')
res.append(
    sum(map(lambda x, i: (-1)**i * x, a[1], range(len(a[1])))) if a[1] else 'N')
res.append(len(a[2]) if a[2] else 'N')
res.append(f'{sum(a[3]) / len(a[3]):.1f}' if a[3] else 'N')
res.append(max(a[4]) if a[4] else 'N')
print(*res)
