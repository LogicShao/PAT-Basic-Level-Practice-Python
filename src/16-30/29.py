a, b = [input().upper() for _ in range(2)]
keyboardlst = list(
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_')
dic = {k: False for k in keyboardlst}
tdic = {k: False for k in keyboardlst}
res = ''
i, j = 0, 0
while j < len(b):
    while i < len(a) and a[i] != b[j]:
        if not dic[a[i]] and not tdic[a[i]]:
            res += a[i]
            tdic[a[i]] = True
        i += 1
    dic[b[j]] = True
    j += 1
    i += 1
while i < len(a):
    if not dic[a[i]] and not tdic[a[i]]:
        dic[a[i]] = True
        res += a[i]
    i += 1
print(res)
