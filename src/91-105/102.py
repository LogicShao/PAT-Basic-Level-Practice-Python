n = int(input())
maxN, maxS = -1, -1
ansN, ansS = "", ""

for _ in range(n):
    name, a, b = input().split()
    a, b = int(a), int(b)
    if b > maxN:
        maxN = b
        ansN = name
    if a * b > maxS:
        maxS = a * b
        ansS = name

print(f"{ansN} {maxN}")
print(f"{ansS} {maxS}")
