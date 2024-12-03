n, k, x = map(int, input().split())
A = []
Sum = [0] * 100  # 假设最大 n 为 100
cnt = 1

# 读取矩阵
for i in range(n):
    A.append(list(map(int, input().split())))
    if i % 2 == 1:  # 奇数行
        for j in range(n):
            Sum[j] += A[i][j]

# 处理偶数行
for i in range(0, n, 2):  # 偶数行索引
    for j in range(cnt):
        Sum[j] += x
    for j in range(cnt, n):
        Sum[j] += A[i][j - cnt]
    cnt = cnt % k + 1

# 输出结果
print(" ".join(map(str, Sum[:n])))
