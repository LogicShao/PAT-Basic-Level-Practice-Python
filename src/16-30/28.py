bound1 = '1814/09/06'
bound2 = '2014/09/06'
n = int(input())
a = []
for i in range(n):
    name, date = input().split()
    if bound1 <= date <= bound2:
        a.append((name, date))
if not a:
    print(0)
else:
    print(len(a), min(a, key=lambda x: x[1])[0], max(
        a, key=lambda x: x[1])[0])
