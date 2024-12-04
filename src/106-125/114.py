def isprime(x):
    if x < 2:
        return False
    i = 2
    while i <= x // i:
        if x % i == 0:
            return False
        i += 1
    return True


s = input()
flag = True
for i in range(len(s)):
    now = s[-i:]
    if isprime(int(now)):
        print(now, 'Yes')
    else:
        print(now, 'No')
        flag = False
if flag:
    print('All Prime!')
