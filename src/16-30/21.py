from collections import Counter

for x, y in sorted(Counter(input()).items()):
    print(f"{x}:{y}")
