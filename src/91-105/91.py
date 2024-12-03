def main():
    m = int(input())
    for k in map(int, input().split()):
        flag = False
        for n in range(1, 10):
            mul = n * k * k
            smul = str(mul)
            sk = str(k)
            smul_end = smul[-len(sk):]
            if smul_end == sk:
                print(n, mul)
                flag = True
                break
        if not flag:
            print("No")


if __name__ == "__main__":
    main()
