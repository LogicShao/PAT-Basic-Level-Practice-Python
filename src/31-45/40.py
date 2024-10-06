s = ' ' + input()
cnt_p = [0 for _ in range(len(s))]
cnt_t = [0 for _ in range(len(s))]
mod = 1000000007
res = 0
for i in range(1, len(s)):
    cnt_p[i] = cnt_p[i - 1] + (s[i] == 'P')
    cnt_t[i] = cnt_t[i - 1] + (s[i] == 'T')
for i in range(1, len(s)):
    if s[i] == 'A':
        res = (res + cnt_p[i] * (cnt_t[-1] - cnt_t[i])) % mod
print(res)
