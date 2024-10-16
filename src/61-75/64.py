from collections import Counter

n = int(input())
cnt = Counter(map(lambda x: sum(map(int, x)), input().split()))
print(len(cnt))
print(*(sorted(cnt.keys())))
