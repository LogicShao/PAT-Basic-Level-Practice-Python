n = int(input())
g = dict()
for i in range(n):
    a, b = input().split()
    g[a] = b
    g[b] = a
m = int(input())
a = input().split()
st = set(a)
res = sorted(filter(lambda x: not (x in st and x in g and g[x] in st), a))
print(len(res))
if res:
    print(*res)
