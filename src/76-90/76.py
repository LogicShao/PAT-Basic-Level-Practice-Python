n = int(input())
res = ''
for i in range(n):
    s = input().split()
    for ss in s:
        a, b = ss.split('-')
        if b == 'T':
            res += str(ord(a) - ord('A') + 1)
print(res)
