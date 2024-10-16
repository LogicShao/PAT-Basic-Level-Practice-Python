m, n, s = map(int, input().split())
a = [input() for _ in range(m)]
res = []
st = set()
i = s - 1
while i < m:
    if a[i] not in st:
        res.append(a[i])
        st.add(a[i])
        i += n
    else:
        i += 1
if res:
    print('\n'.join(res))
else:
    print('Keep going...')
