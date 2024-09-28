def change(x, k):
    if x == 0:
        return '0'
    res = ''
    while x:
        res = str(x % k) + res
        x //= k
    return res


a, b, d = map(int, input().split())
print(change(a + b, d))
