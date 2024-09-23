n = int(input())
st = set()
a = list(map(int, input().split()))
for i in a:
    while i != 1:
        if i % 2 == 0:
            i = i // 2
        else:
            i = (3 * i + 1) // 2
        if i in st:
            break
        st.add(i)
res = sorted(list(filter(lambda x: x not in st, a)), reverse=True)
print(' '.join(map(str, res)))