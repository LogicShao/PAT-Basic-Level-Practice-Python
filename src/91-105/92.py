def main():
    m, n = map(int, input().split())
    sums = [0] * (m + 1)
    maxn = 0
    ans = []

    for _ in range(n):
        for temp, j in zip(map(int, input().split()), range(1, m + 1)):
            sums[j] += temp
            maxn = max(maxn, sums[j])

    print(maxn)
    for i in range(1, m + 1):
        if sums[i] == maxn:
            ans.append(i)

    print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()
