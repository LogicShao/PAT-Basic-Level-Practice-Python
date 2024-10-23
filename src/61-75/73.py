n, m = map(int, input().split())
answers = []
scores = []
nums = []
ok_nums = []
for i in range(m):
    data = list(map(lambda x: int(x) if x.isdigit() else x, input().split()))
    scores.append(data[0])
    nums.append(data[1])
    ok_nums.append(data[2])
    answers.append(set(data[3:]))
tasks = [dict(zip('abcde', [0] * 5)) for _ in range(m)]
for i in range(n):
    data = list(map(lambda x: int(x) if x.isdigit() else x,
                input().replace('(', '').replace(')', '').split()))
    score = 0
    for j in range(m):
        num = data[0]
        ans = set(data[1:1 + num])
        if ans == answers[j]:
            score += scores[j]
        elif ans & answers[j] == ans:
            score += scores[j] / 2
        if ans != answers[j]:
            for x in filter(lambda x: x not in answers[j], ans):
                tasks[j][x] += 1
            for x in filter(lambda x: x not in ans, answers[j]):
                tasks[j][x] += 1
        data = data[1 + num:]
    print('%.1f' % score)
maxn = max(y for x in tasks for y in x.values())
if maxn == 0:
    print('Too simple')
else:
    for i in range(m):
        for j in 'abcde':
            if tasks[i][j] == maxn:
                print('{} {}-{}'.format(maxn, i + 1, j))
