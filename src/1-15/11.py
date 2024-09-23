n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
print('\n'.join('Case #%d: %s' % (i + 1, str(x + y > z).lower())
      for i, (x, y, z) in enumerate(a)))
