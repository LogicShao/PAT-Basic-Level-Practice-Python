s = input()
p = input()
snxtchar = [dict(zip(range(26), [-1] * 26))
            for _ in range(len(s))]
for i in range(len(s) - 2, -1, -1):
    snxtchar[i] = snxtchar[i + 1].copy()
    snxtchar[i][ord(s[i + 1]) - ord('a')] = i + 1
res = [0, len(s)-1]
for i in range(len(s)):
    if s[i] != p[0]:
        continue
    j = i
    for k in range(1, len(p)):
        if snxtchar[j][ord(p[k]) - ord('a')] == -1:
            break
        j = snxtchar[j][ord(p[k]) - ord('a')]
    else:
        if j - i < res[1] - res[0]:
            res[0], res[1] = i, j
print(s[res[0]:res[1]+1])
