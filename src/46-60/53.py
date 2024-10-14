def mcheck(x): return float(x) if x.find('.') != -1 else int(x)


n, e, d = map(mcheck, input().split())
a = [list(map(mcheck, input().split())) for _ in range(n)]
res1, res2 = 0, 0
for i, k in enumerate(a):
    flag1 = len([i for i in k[1:] if i < e]) > k[0] / 2
    flag2 = k[0] > d
    if flag1 and flag2:
        res2 += 1
    elif flag1:
        res1 += 1
print('{:.1f}% {:.1f}%'.format(res1 / n * 100, res2 / n * 100))
