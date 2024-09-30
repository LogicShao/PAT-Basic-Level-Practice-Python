from collections import Counter

n = int(input())
a = Counter(map(int, input().split()))
print(*(a[i] for i in list(map(int, input().split()))[1:]))
