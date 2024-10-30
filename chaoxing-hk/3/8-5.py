def getMaxMinLen(lst):
    return max(lst), min(lst), len(lst)


sl = [9, 7, 8, 3, 2, 1, 55, 6]
s2 = ["apple", "pear", "melon", "kiwi"]
s3 = "TheQuickBrownFox"

for s in (sl, s2, s3):
    print('list=', s)
    print('最大值= {}，最小值= {}，元素个数= {}'.format(*getMaxMinLen(s)))
