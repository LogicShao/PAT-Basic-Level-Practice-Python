b, a = map(lambda x: list(map(int, x.split('.'))), input().split())
base = [0, 17, 29]
c = []
if a < b:
    a, b = b, a
    print('-', end='')
for i, (j, k) in enumerate(zip(a, b)):
    c.append(j - k)
    while i and c[i] < 0:
        c[i] += base[i]
        c[i - 1] -= 1
        i -= 1
print('.'.join(map(str, c)))
