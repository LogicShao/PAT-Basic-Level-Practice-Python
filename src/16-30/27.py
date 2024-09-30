n, c = input().split()
n, k = int(n) - 1, 2
while True:
    cnt = (2 * k - 1) * 2
    if n < cnt:
        k -= 1
        break
    n -= cnt
    k += 1
l, r = 1, 2 * k - 1
for i in range(1, 2 * k):
    ll, rr = min(l, r), max(l, r)
    line = ' ' * (ll - 1) + c * (rr - ll + 1)
    print(line)
    l += 1
    r -= 1
print(n)
