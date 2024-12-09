nums = set(map(int, input().split()))
n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
status = [True] * n
for round in range(m):
    for i in range(n):
        if not status[i]:
            continue
        nowNum = data[i][round]
        if nowNum in nums or all(num + nowNum not in nums for num in nums):
            status[i] = False
            print('Round #{}: {} is out.'.format(round + 1, i + 1))
            continue
        nums.add(nowNum)
winners = list(filter(lambda x: status[x], range(n)))
if winners:
    print('Winner(s):', ' '.join(map(lambda x: str(x+1), winners)))
else:
    print('No winner.')
