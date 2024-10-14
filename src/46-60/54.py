def wrong(s):
    print('ERROR: {} is not a legal number'.format(s))
    return False


def mcheck(s):
    try:
        val = eval(s)
    except:
        return wrong(s)
    if val < -1000 or val > 1000:
        return wrong(s)
    pos = s.find('.')
    if pos != -1 and len(s) - pos > 3:
        return wrong(s)
    return True


n = int(input())
a = [float(i) for i in input().split() if mcheck(i)]
if len(a) == 0:
    print('The average of 0 numbers is Undefined')
elif len(a) == 1:
    print('The average of 1 number is {:.2f}'.format(a[0]))
else:
    print('The average of {} numbers is {:.2f}'.format(len(a), sum(a) / len(a)))
