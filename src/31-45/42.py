from collections import Counter

cnt = Counter(filter(lambda x: x.isalpha(), input().lower()))
times = max(cnt.values())
for c in map(chr, range(97, 123)):
    if cnt[c] == times:
        print(c, times)
        break
