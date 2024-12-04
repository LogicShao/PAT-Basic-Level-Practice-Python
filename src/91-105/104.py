import math
from math import gcd


class Node:
    def __init__(self, n, num):
        self.n = n
        self.num = num

    def __lt__(self, other):
        if self.n != other.n:
            return self.n < other.n
        return self.num < other.num


def is_prime(x):
    if x <= 2:
        return 0
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return 0
    return 1


N = int(input())
for case in range(1, N + 1):
    print(f"Case {case}")
    K, m = map(int, input().split())
    if K * 9 < m:
        print("No Solution")
    else:
        A = []
        temp = 10**(K - 2)
        for i in range(temp // 10, temp):
            sum_digits = 18
            sum2 = 0
            I = i
            II = i + 1

            while I:
                sum_digits += I % 10
                I //= 10
                if sum_digits > m:
                    break

            while II:
                sum2 += II % 10
                II //= 10

            if sum_digits == m and is_prime(gcd(m, sum2)):
                A.append(Node(sum2, i))

        A.sort()
        if not A:
            print("No Solution")
        else:
            for node in A:
                print(f"{node.n} {node.num}99")
