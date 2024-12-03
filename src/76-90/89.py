def main():
    n = int(input())
    v = [0] + [int(input()) for _ in range(n)]

    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            lie = []
            a = [1] * (n + 1)
            a[i] = a[j] = -1

            for k in range(1, n + 1):
                if v[k] * a[abs(v[k])] < 0:
                    lie.append(k)

            if len(lie) == 2 and a[lie[0]] + a[lie[1]] == 0:
                print(i, j)
                return

    print("No Solution")


main()
