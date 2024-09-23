s = input()
a, b, c = map(int, '0' * (3 - len(s)) + s)
print('B' * a + 'S' * b + ''.join(str(i) for i in range(1, c+1)))