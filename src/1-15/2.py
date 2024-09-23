s = input()
n = sum(map(int, s))
pinying = ['ling', 'yi', 'er', 'san', 'si', 'wu', 'liu', 'qi', 'ba', 'jiu']
print(' '.join(pinying[int(i)] for i in str(n)))
