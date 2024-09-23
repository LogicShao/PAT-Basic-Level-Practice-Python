T = int(input())
for _ in range(T):
    s = input()
    p_pos = s.find('P')
    t_pos = s.find('T')
    if p_pos == -1 or t_pos == -1 or p_pos >= t_pos:
        print('NO')
        continue
    t = [s[:p_pos], s[p_pos+1:t_pos], s[t_pos+1:]]
    if any(map(lambda x: x.count('A') != len(x), t)) or t[1] == '' or len(t[0]) * len(t[1]) != len(t[2]):
        print('NO')
        continue
    print('YES')
