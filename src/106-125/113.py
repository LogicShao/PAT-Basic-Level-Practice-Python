tmp = '0123456789abcdefghijklmnopqrstuvwxyz'
basedic = dict(zip(tmp, range(len(tmp))))


def todec(s, base):
    res = 0
    for c in s:
        res = res * base + basedic[c]
    return res


def tobase(n, base):
    res = ''
    while n:
        res += tmp[n % base]
        n //= base
    return res[::-1] or '0'


a, b = map(todec, input().split(), [30] * 2)
print(tobase(a + b, 30))
