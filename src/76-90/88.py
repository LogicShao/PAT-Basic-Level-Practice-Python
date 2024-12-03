import math

def print_relation(m, t):
    if m == t:
        print(" Ping", end="")
    elif m < t:
        print(" Cong", end="")
    else:
        print(" Gai", end="")

def main():
    m, x, y = map(int, input().split())
    for i in range(99, 9, -1):
        j = (i % 10) * 10 + (i // 10)
        k = abs(j - i) / x
        if j == k * y:
            print(i, end="")
            print_relation(m, i)
            print_relation(m, j)
            print_relation(m, k)
            return
    print("No Solution")

main()
