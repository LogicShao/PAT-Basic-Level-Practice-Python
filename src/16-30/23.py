cnt = list(map(int, input().split()))
res = ''.join(str(i) * cnt[i] for i in range(1, 10))
res = res[0] + '0' * cnt[0] + res[1:]
print(res)
