# 编写程序，产生两个0~100（包含0和100）的随机整数a和b，求这两个整数的最大公约数和最小公倍数

import random

a = random.randint(0, 100)
b = random.randint(0, 100)


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return a * b // gcd(a, b)


print(f"整数1 = {a}，整数2 = {b}\n最大公约数 = {gcd(a, b)}，最小公倍数 = {lcm(a, b)}")