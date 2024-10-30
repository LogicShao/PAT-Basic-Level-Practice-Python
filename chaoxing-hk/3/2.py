toRemove = '.,:;!?'
s = input('请输入字符串：')
for i in toRemove:
    s.replace(i, '')
cnt = len(s.split())
print('单词数为：{}'.format(cnt))