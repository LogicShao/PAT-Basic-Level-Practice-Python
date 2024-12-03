op = input()
s = input()
if op == 'C':
    res = ''
    i = 0
    while i < len(s):
        j = i
        while j < len(s) and s[j] == s[i]:
            j += 1
        if j - i > 1:
            res += str(j - i) + s[i]
        else:
            res += s[i]
        i = j
    print(res)
else:
    res = ''
    i = 0
    while i < len(s):
        if s[i].isdigit():
            j = i + 1
            while j < len(s) and s[j].isdigit():
                j += 1
            res += s[j] * int(s[i:j])
            i = j + 1
        else:
            res += s[i]
            i += 1
    print(res)
