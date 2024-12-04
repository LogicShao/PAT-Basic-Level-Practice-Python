input()
arr = map(int, input().split())
arr = list(filter(lambda v: v % 2 == 1, arr))
result = arr[0]
for i in range(1, len(arr)):
    result ^= arr[i]
print(result)
