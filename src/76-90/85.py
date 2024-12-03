n = int(input())
data = {}
weight = dict(zip('ABT', [1, 1/1.5, 1.5]))
for i in range(n):
    Id, score, college = input().split()
    college = college.lower()
    score = int(score) * weight[Id[0]]
    if college not in data:
        data[college] = [score, 1]
    else:
        data[college][0] += score
        data[college][1] += 1
for college in data:
    data[college][0] //= 1
data = sorted(data.items(), key=lambda x: (-x[1][0], x[1][1], x[0]))
print(len(data))
rank = 1
for i, (college, score) in enumerate(data):
    if i > 0 and score[0] != data[i-1][1][0]:
        rank = i + 1
    print(rank, college, int(score[0]), score[1])
