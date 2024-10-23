x, k = map(int, input().split())
for i in range(k):
    n1, b, t, n2 = map(int, input().split())
    if t > x:
        print('Not enough tokens.  Total = {}.'.format(x))
        continue
    if b == 0:
        if n1 < n2:
            x -= t
            print('Lose {}.  Total = {}.'.format(t, x))
        else:
            x += t
            print('Win {}!  Total = {}.'.format(t, x))
    else:
        if n1 > n2:
            x -= t
            print('Lose {}.  Total = {}.'.format(t, x))
        else:
            x += t
            print('Win {}!  Total = {}.'.format(t, x))
    if x == 0:
        print('Game Over.')
        break
