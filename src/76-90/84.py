d, n = map(int, input().split())
res = str(d)
for i in range(n - 1):
    nxt = ''
    i = 0
    while i < len(res):
        cnt = 1
        while i + 1 < len(res) and res[i] == res[i + 1]:
            i += 1
            cnt += 1
        nxt += res[i] + str(cnt)
        i += 1
    res = nxt
print(res)
