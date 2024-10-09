a, b = input().split()
to = "0123456789JQK"
res = ""
if len(a) < len(b):
    a = "0" * (len(b) - len(a)) + a
else:
    b = "0" * (len(a) - len(b)) + b
for i in range(1, min(len(a), len(b)) + 1):
    if i % 2 == 1:
        res += to[(to.index(b[-i]) + to.index(a[-i])) % 13]
    else:
        res += to[(to.index(b[-i]) - to.index(a[-i]) + 10) % 10]
print(res[::-1])
