def check(x):
    s = str(x)
    return s == s[::-1]


x = int(input())
step = 0
while not check(x) and step < 10:
    print(x, '+', str(x)[::-1], '=', x + int(str(x)[::-1]))
    x += int(str(x)[::-1])
    step += 1
if check(x):
    print(x, 'is a palindromic number.')
else:
    print('Not found in 10 iterations.')
