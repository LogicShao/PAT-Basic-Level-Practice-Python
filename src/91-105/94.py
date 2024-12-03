def isprime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


l, k = map(int, input().split())
s = input()
for i in range(l - k + 1):
    n = s[i:i + k]
    if isprime(int(n)):
        print(n)
        break
else:
    print('404')
