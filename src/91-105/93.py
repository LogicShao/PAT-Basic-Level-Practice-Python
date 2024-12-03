a = input()
b = input()
res = ''
st = set()
for i in a + b:
    if i not in st:
        res += i
        st.add(i)
print(res)
