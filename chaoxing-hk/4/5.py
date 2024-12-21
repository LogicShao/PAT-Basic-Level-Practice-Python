from random import randint

a = set(randint(0, 10) for _ in range(10))
b = set(randint(0, 10) for _ in range(10))
print('集合的内容、长度、最大值、最小值分别为：')
print(a, len(a), max(a), min(a))
print(b, len(b), max(b), min(b))
print('A和B的并集、交集、差集分别为：')
print(a | b, a & b, a - b)
