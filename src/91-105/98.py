n = int(input())
minA = min(*map(int, input().split()), 2000)
maxB = max(*map(int, input().split()), 0)

# 输出结果
if minA <= maxB:
    print(f"No {maxB - minA + 1}")
else:
    print(f"Yes {minA - maxB}")
