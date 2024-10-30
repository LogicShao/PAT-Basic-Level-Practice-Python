heads = int(input('请输入总头数：'))
while (legs := int(input('请输入总腿数(必须是偶数)：'))) % 2 != 0:
    pass


def solve1(heads, legs):
    rabbits = legs // 2 - heads
    chickens = heads - rabbits
    if chickens >= 0 and rabbits >= 0:
        print('方法一：鸡：{}只，兔：{}只'.format(chickens, rabbits))
    else:
        print('方法一：无解，请重新运行测试！')


def solve2(heads, legs):
    for chickens in range(heads + 1):
        rabbits = heads - chickens
        if 2 * chickens + 4 * rabbits == legs:
            print('方法二：鸡：{}只，兔：{}只'.format(chickens, rabbits))
            break
    else:
        print('方法二：无解，请重新运行测试！')


if __name__ == '__main__':
    solve1(heads, legs)
    solve2(heads, legs)
