s = [9, 7, 8, 3, 2, 1, 5, 6]
print('变换前，s=', s)
s = list(map(lambda x: x**2 if x % 2 == 0 else x, s))
print('变换后，s=', s)
