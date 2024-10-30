height = 100
total = 100
for i in range(9):
    total += height
    height /= 2
print('小球在第10次落地时，共经过{}米，第10次反弹{}米'.format(total, height / 2))
