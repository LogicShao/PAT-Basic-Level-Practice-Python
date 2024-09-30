from collections import Counter

a = Counter(input())
b = Counter(input())
c = a & b
if c == b:
    print("Yes", sum(a.values()) - sum(b.values()))
else:
    print("No", sum(b.values()) - sum(c.values()))
