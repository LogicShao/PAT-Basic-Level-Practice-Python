n, m = map(int, input().split())
st = set(input().split())
data = [input().split() for _ in range(n)]
res = [[i[0] + ':'] + [x for x in i[1:] if x in st] for i in data]
res = [i for i in res if len(i) > 1]
if res:
    print('\n'.join([' '.join(i) for i in res]))
print(len(res), sum([len(i) - 1 for i in res]))
