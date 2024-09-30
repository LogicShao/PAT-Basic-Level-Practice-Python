n, c = input().split()
n = int(n)
for i in range((n + 1) // 2):
    if i == 0 or i == (n + 1) // 2 - 1:
        print(c * n)
    else:
        print(c + ' ' * (n - 2) + c)
