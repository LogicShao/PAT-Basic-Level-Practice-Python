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


n = int(input())
p, st = getPrimes(n)
print(sum(p[i] - p[i - 1] == 2 for i in range(1, len(p))))
