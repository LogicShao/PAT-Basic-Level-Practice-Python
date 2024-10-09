n = int(input())
dic = {}
for i in range(n):
    a, b, c = input().split()
    dic[b] = (a, c)
m = int(input())
print('\n'.join(' '.join(dic[a]) for a in input().split()))
