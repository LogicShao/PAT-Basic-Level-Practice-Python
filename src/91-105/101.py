x, k = input().split()
k = int(k)
a = int(x)
b = int(x[-k:] + x[:-k])
print('{:.2f}'.format(b / a))
