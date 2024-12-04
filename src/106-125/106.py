n = int(input())
f = list(map(int, "2019"))
for i in range(n - 4):
    f.append(sum(f[-4:]) % 10)
print("".join(map(str, f[:n])))
