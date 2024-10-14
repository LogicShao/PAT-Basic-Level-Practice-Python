a = list(map(int, input().split()))[1:]
st = set()
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        st.add(10 * a[i] + a[j])
        st.add(10 * a[j] + a[i])
print(sum(filter(lambda x: x in st, range(10, 100))))
