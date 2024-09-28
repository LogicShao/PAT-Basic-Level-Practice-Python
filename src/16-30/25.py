head, n, k = input().split()
n, k = int(n), int(k)
link = {}
for i in range(n):
    addr, data, nxt = input().split()
    link[addr] = [data, nxt]
data = []
cnt = 0
curr = head
while curr != '-1':
    data.append(curr)
    curr = link[curr][1]
for i in range(0, len(data), k):
    if i + k <= len(data):
        data[i:i + k] = data[i:i + k][::-1]
if n != 1:
    print('\n'.join('%s %s %s' % (data[i], link[data[i]][0], data[i + 1])
                    for i in range(len(data) - 1)))
print('%s %s -1' % (data[-1], link[data[-1]][0]))
