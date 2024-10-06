from collections import Counter

cnt = Counter(filter(lambda x: x in "PATest", input()))
n = sum(cnt.values())
res = ""
while n > 0:
    for c in "PATest":
        if cnt[c] > 0:
            res += c
            cnt[c] -= 1
            n -= 1
print(res)
