def foo(s, d):
    s = list(map(int, str(s)))
    cnt = s.count(d)
    if cnt == 0:
        return 0
    return int(str(d) * cnt)


a, b, c, d = map(int, input().split())
print(foo(a, b) + foo(c, d))
