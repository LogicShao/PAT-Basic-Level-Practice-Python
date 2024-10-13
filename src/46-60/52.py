import sys


def getIt(s):
    res = []
    i = 0
    while i < len(s):
        if s[i] == '[':
            t = ''
            j = i + 1
            while j < len(s) and s[j] != ']':
                t += s[j]
                j += 1
            if j != len(s):
                res.append(t)
            i = j + 1
        else:
            i += 1
    return res


def minput():
    data = sys.stdin.buffer.readline().strip()
    i = 0
    result = []
    while i < len(data):
        if data[i] <= 127:
            # ASCII 字符，一个字节处理
            result.append(chr(data[i]))
            i += 1
        else:
            # 非 ASCII 字符，两个字节处理
            if i + 1 < len(data):
                result.append(data[i:i+2].decode('utf-8', errors='ignore'))
                i += 2
            else:
                # 如果最后一个字节是非 ASCII 字符且没有足够的字节组成一个字符
                result.append(chr(data[i]))
                i += 1
    return ''.join(result)


hand = getIt(minput())
eye = getIt(minput())
mouth = getIt(minput())
od = [hand, eye, mouth, eye, hand]
n = int(minput())
for _ in range(n):
    lst = list(map(int, minput().split()))
    if len(lst) != 5 or any(lst[i] < 1 or lst[i] > len(od[i]) for i in range(5)):
        print('Are you kidding me? @\\/@')
        continue
    res = "{}({}{}{}){}".format(*(od[i][lst[i] - 1] for i in range(5)))
    print(res)
