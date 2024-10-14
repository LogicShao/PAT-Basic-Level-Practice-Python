n = int(input())
a = sorted(map(int, input().split()))
for i in range(n, 0, -1):
    if a[n - i] > i:
        print(i)
        break
else:
    print(0)
