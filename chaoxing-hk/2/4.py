import random


def getThreeRandomNumbers():
    return random.sample(range(0, 101), 3)


def solve1(a, b, c):
    if a > b:
        a, b = b, a
    if a > c:
        a, c = c, a
    if b > c:
        b, c = c, b
    print('(方法一)升序值： a={}， b={}， c={}'.format(a, b, c))


def solve2(a, b, c):
    a, b, c = min(a, b, c), a + b + c - max(a, b, c) - \
        min(a, b, c), max(a, b, c)
    print('(方法二)升序值： a={}， b={}， c={}'.format(a, b, c))


if __name__ == '__main__':
    a, b, c = getThreeRandomNumbers()
    print('原始值：a={}， b={}， c={}'.format(a, b, c))
    solve1(a, b, c)
    solve2(a, b, c)
