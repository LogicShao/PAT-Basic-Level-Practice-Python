x = bin(sum(map(lambda s: ord(s) - ord('a') + 1,
        filter(lambda s: s.isalpha(), input().lower()))))[2:]
if x == '0':
    print(0, 0)
else:
    print(x.count('0'), x.count('1'))
