from collections import Counter

n = int(input())
data = []
for i, x in enumerate(map(int, input().split())):
    data.append(abs(i + 1 - x))
data = Counter(data)
data = sorted(data.items(), key=lambda x: x[0], reverse=True)
for k, v in data:
    if v > 1:
        print(k, v)
