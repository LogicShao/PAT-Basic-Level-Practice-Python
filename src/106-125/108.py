from collections import Counter

s = input()
cnt = Counter(s)
res = ''
t = "String"
i = 0
while any(cnt[c] for c in t):
    if cnt[t[i]]:
        res += t[i]
        cnt[t[i]] -= 1
    i = (i + 1) % 6
print(res)
