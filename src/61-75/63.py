n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
a = list(map(lambda x: (x[0]**2 + x[1]**2)**0.5, a))
print('{:.2f}'.format(max(a)))
