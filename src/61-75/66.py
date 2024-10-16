n, m, A, B, Tar = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]
for line in g:
    line = list(map(lambda x: Tar if A <= x <= B else x, line))
    print(*map(str.format, ['{:03}'] * m, line))
