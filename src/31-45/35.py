n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
i = 0
while i < n - 1 and b[i] <= b[i + 1]:
    i += 1
j = i + 1
while j < n and a[j] == b[j]:
    j += 1
if j == n:
    print('Insertion Sort')
    a[:i + 2] = sorted(a[:i + 2])
else:
    print('Merge Sort')
    k = 1
    flag = True
    while flag:
        flag = False
        k *= 2
        for i in range(n):
            if a[i] != b[i]:
                flag = True
        for i in range(0, n, k):
            a[i:i + k] = sorted(a[i:i + k])
print(*a)
