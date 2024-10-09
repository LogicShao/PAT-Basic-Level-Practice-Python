n = int(input())
dic = {}
for i in range(n):
    a, b = input().split()
    a = int(a.split('-')[0])
    b = int(b)
    dic[a] = dic.get(a, 0) + b
print(*max(dic.items(), key=lambda x: x[1]))
