p, m, n = map(int, input().split())
pscore = {}
mscore = {}
nscroe = {}
students = set()
for i in range(p):
    a, b = input().split()
    pscore[a] = int(b)
    students.add(a)
for i in range(m):
    a, b = input().split()
    mscore[a] = int(b)
    students.add(a)
for i in range(n):
    a, b = input().split()
    nscroe[a] = int(b)
    students.add(a)
res = []
for stu in students:
    Gonline = pscore.get(stu, -1)
    Gmidterm = mscore.get(stu, -1)
    Gfinal = nscroe.get(stu, -1)
    if Gmidterm > Gfinal:
        G = round(Gmidterm * 0.4 + Gfinal * 0.6)
    else:
        G = Gfinal
    if Gonline >= 200 and G >= 60:
        res.append([stu, Gonline, Gmidterm, Gfinal, G])
res.sort(key=lambda x: (-x[4], x[0]))
for i in res:
    print(*i)
