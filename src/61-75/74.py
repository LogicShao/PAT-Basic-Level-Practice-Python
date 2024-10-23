b = list(map(int, reversed(input())))
x = list(map(int, reversed(input())))
y = list(map(int, reversed(input())))
if len(x) > len(y):
    y += [0] * (len(x) - len(y))
else:
    x += [0] * (len(y) - len(x))
c = [0] * (len(x) + 1)
for i in range(len(x)):
    base = b[i] if b[i] else 10
    c[i] += x[i] + y[i]
    c[i + 1] = c[i] // base
    c[i] %= base
while len(c) > 1 and c[-1] == 0:
    c.pop()
print(''.join(map(str, reversed(c))))
