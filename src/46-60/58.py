n, m = map(int, input().split())
answers = [set(input().split()[3:]) for _ in range(m)]
tasks = [0 for _ in range(m)]
for i in range(n):
    s = input().replace('(', '').replace(')', '').split()
    cnt = 0
    for j in range(m):
        nowans = set(s[1:1 + int(s[0])])
        if nowans == answers[j]:
            tasks[j] += 1
            cnt += 1
        s = s[1 + int(s[0]):]
    print(cnt)
if any(tasks):
    mxval = max(tasks)
    print(' '.join(str(i + 1) for i in range(m) if tasks[i] == mxval))
else:
    print('Too simple')
