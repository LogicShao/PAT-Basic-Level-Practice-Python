def isprime(x):
    if x == 2:
        return True
    if x < 2 or x % 2 == 0:
        return False
    for i in range(3, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            return False
    return True


n = int(input())
dic = dict(zip((input() for _ in range(n)), range(1, n + 1)))
m = int(input())
checked = set()
for i in range(m):
    ID = input()
    if ID not in dic:
        print('{}: Are you kidding?'.format(ID))
        continue
    if ID in checked:
        print('{}: Checked'.format(ID))
        continue
    checked.add(ID)
    rnk = dic[ID]
    if rnk == 1:
        print('{}: Mystery Award'.format(ID))
    elif isprime(rnk):
        print('{}: Minion'.format(ID))
    else:
        print('{}: Chocolate'.format(ID))
