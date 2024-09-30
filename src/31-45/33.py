badkey, s = input(), input()
chrlst = list(
    'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_,.-')
ok = {k: True for k in chrlst}
if '+' in badkey:
    for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        ok[c] = False
for c in badkey:
    if c == '+':
        continue
    if c.isalpha():
        ok[c.lower()] = False
        ok[c.upper()] = False
    else:
        ok[c] = False
print(''.join(filter(lambda x: ok[x], s)))
