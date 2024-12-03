n = int(input())
for i in range(n):
    pd = input()
    if len(pd) < 6:
        print('Your password is tai duan le.')
        continue
    if not any(c.isdigit() for c in pd):
        print('Your password needs shu zi.')
        continue
    if not any(c.isalpha() for c in pd):
        print('Your password needs zi mu.')
        continue
    if any(not(c.isalnum() or c == '.') for c in pd):
        print('Your password is tai luan le.')
        continue
    print('Your password is wan mei.')
