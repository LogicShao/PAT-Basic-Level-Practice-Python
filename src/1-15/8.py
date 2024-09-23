n, m = map(int, input().split())
a = list(map(int, input().split()))
m %= n
print(*(a[-m:] + a[:-m]))
