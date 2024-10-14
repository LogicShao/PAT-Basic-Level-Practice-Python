n, k = map(int, input().split())
a = sorted([input().split() for _ in range(n)],
           key=lambda x: (-int(x[1]), x[0]), reverse=True)
res = [[0] * (n - (n // k) * (k - 1))] + [[0] * (n // k)
                                          for _ in range(k - 1)]
p = 0
for k in res[::-1]:
    i, j = 0, len(k) - 1
    for t in range(len(k)):
        if t % 2 != len(k) % 2:
            k[j] = a[p][0]
            j -= 1
        else:
            k[i] = a[p][0]
            i += 1
        p += 1
print('\n'.join(' '.join(i) for i in res))
