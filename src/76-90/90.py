def main():
    from collections import defaultdict

    n, k = map(int, input().split())
    m = defaultdict(list)

    for _ in range(n):
        t1, t2 = map(int, input().split())
        m[t1].append(t2)
        m[t2].append(t1)

    for _ in range(k):
        v = list(map(int, input().split()))[1:]
        a = set(v)
        flag = False

        for x in v:
            for neighbor in m[x]:
                if neighbor in a:
                    flag = True
                    break
            if flag:
                break

        print("No" if flag else "Yes")


if __name__ == "__main__":
    main()
