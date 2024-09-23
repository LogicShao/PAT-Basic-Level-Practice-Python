import os

srcdir = './src/'

# 一共 75 道题目
# 15 道题目一个文件夹
# 创建 5 个文件夹
for i in range(1, 6):
    if not os.path.exists(srcdir + str(i)):
        os.mkdir(srcdir + '{}-{}'.format((i-1)*15+1, i*15))
