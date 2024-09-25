def getPrimes(N):
    primes = []
    st = [False] * (N + 1)
    for i in range(2, N + 1):
        if not st[i]:
            primes.append(i)
        for j in primes:
            if i * j > N:
                break
            st[i * j] = True
            if i % j == 0:
                break
    return primes, st


p, st = getPrimes(104729)
l, r = map(int, input().split())
ans = p[l - 1:r]
for i in range(0, len(ans), 10):
    print(*ans[i:i + 10])
