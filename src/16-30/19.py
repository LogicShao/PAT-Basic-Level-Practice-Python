n = input()
if len(set(n)) == 1 and len(n) == 4:
    print(f'{n} - {n} = 0000')
else:
    while True:
        n = ''.join(sorted(n.zfill(4), reverse=True))
        print(f'{n} - {n[::-1]} = {int(n) - int(n[::-1]):04d}')
        n = str(int(n) - int(n[::-1])).zfill(4)
        if n == '6174':
            break
