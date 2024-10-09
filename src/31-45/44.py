lst0 = ['tret', 'jan', 'feb', 'mar', 'apr', 'may',
        'jun', 'jly', 'aug', 'sep', 'oct', 'nov', 'dec']
lst1 = ['tret', 'tam', 'hel', 'maa', 'huh', 'tou',
        'kes', 'hei', 'elo', 'syy', 'lok', 'mer', 'jou']


def earth2mars(earth):
    if earth == '0':
        return 'tret'
    num = int(earth)
    if num // 13 == 0:
        return lst0[num % 13]
    elif num % 13 == 0:
        return lst1[num // 13]
    else:
        return lst1[num // 13] + ' ' + lst0[num % 13]


def mars2earth(mars):
    if mars == 'tret':
        return 0
    lst = mars.split()
    if len(lst) == 1:
        if lst[0] in lst0:
            return lst0.index(lst[0])
        else:
            return lst1.index(lst[0]) * 13
    else:
        return lst1.index(lst[0]) * 13 + lst0.index(lst[1])


n = int(input())
for i in range(n):
    line = input()
    if line.isdigit():
        print(earth2mars(line))
    else:
        print(mars2earth(line))
