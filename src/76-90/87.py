n = int(input())
print(len(set(i // 2 + i // 3 + i // 5 for i in range(1, n + 1))))
