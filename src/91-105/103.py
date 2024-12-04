import math

m, n = map(int, input().split())
record = {}
flag = False

for a in range(m, n + 1):
    d = a**3 - (a - 1)**3
    c = int(math.sqrt(d))
    if c * c != d:
        continue

    for b in range(1, c):
        if b in record:
            temp = record[b]
        else:
            temp = b**2 + (b - 1)**2
            record[b] = temp

        if temp == c:
            print(a, b)
            flag = True
            break

if not flag:
    print("No Solution")
