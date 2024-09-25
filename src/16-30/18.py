n = int(input())
a, b, c = 0, 0, 0
cnt1 = {"C": 0, "J": 0, "B": 0}
cnt2 = {"C": 0, "J": 0, "B": 0}
for _ in range(n):
    s = input()
    i, j = s.split()
    if s == "C J" or s == "J B" or s == "B C":
        a += 1
        cnt1[i] += 1
    elif i == j:
        b += 1
    else:
        c += 1
        cnt2[j] += 1
print(a, b, c)
print(c, b, a)
print(max(cnt1, key=lambda k: (cnt1[k], -ord(k))),
      max(cnt2, key=lambda k: (cnt2[k], -ord(k))))
