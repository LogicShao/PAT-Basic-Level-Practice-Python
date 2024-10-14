n, m = map(int, input().split())
scores, answers = [], []
for i in range(m):
    s = input().split()
    scores.append(int(s[0]))
    answers.append(set(s[3:]))
tasks = [0 for _ in range(m)]
for i in range(n):
    s = input().replace('(', '').replace(')', '').split()
    cnt = 0
    for j in range(m):
        nowans = set(s[1:1 + int(s[0])])
        if nowans == answers[j]:
            cnt += scores[j]
        else:
            tasks[j] += 1
        s = s[1 + int(s[0]):]
    print(cnt)
if any(tasks):
    mxval = max(tasks)
    print(mxval, ' '.join(str(i + 1) for i in range(m) if tasks[i] == mxval))
else:
    print('Too simple')
