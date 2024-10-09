cnt1, cnt2 = 0, 0
for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    if b == a + c and d != a + c:
        cnt2 += 1
    elif b != a + c and d == a + c:
        cnt1 += 1
print(cnt1, cnt2)
