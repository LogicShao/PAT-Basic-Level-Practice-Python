Pn = 1
print('第 {} 天桃子数为：{}'.format(8, Pn))
for i in range(7, 0, -1):
    Pn = (Pn + 1) * 2
    print('第 {} 天桃子数为：{}'.format(i, Pn))
