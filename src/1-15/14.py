week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
a, b, c, d = [input() for _ in range(4)]
flag = 1
for x, y in zip(a, b):
    if flag == 1 and 'A' <= x <= 'G' and x == y:
        wk = week[ord(x) - ord('A')]
        flag = 2
    elif flag == 2 and (x.isnumeric() or 'A' <= x <= 'N') and x == y:
        if x.isnumeric():
            hh = '0' + x
        else:
            hh = str(ord(x) - ord('A') + 10)
        break
for i, (x, y) in enumerate(zip(c, d)):
    if x.isalpha() and x == y:
        mm = str(i).zfill(2)
        break
print(f"{wk} {hh}:{mm}")
