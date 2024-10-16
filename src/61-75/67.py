passwd, times = input().split()
times = int(times)
cnt = 0
while True:
    s = input()
    if s == '#':
        break
    if s == passwd:
        print('Welcome in')
        break
    else:
        print('Wrong password: {}'.format(s))
        cnt += 1
        if cnt == times:
            print('Account locked')
            break
