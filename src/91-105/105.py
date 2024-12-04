import os
import sys
from io import BytesIO, IOBase

_str = str
str = lambda x=b"": x if type(x) is bytes else _str(x).encode()
BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(str(s))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
def input(): return sys.stdin.readline().rstrip("\r\n")
def write(x): sys.stdout.write(str(x))


class Node:
    def __init__(self, data=0, next=-1):
        self.data = data
        self.next = next


MAX_NODES = 100000
A = [Node() for _ in range(MAX_NODES)]
L1, L2, ans = [], [], []

sa, sb, n = map(int, input().split())
for _ in range(n):
    a, data, next_node = map(int, input().split())
    A[a] = Node(data, next_node)

# 构建 L1 链表
ta = sa
while ta != -1:
    L1.append(ta)
    ta = A[ta].next

# 构建 L2 链表
tb = sb
while tb != -1:
    L2.append(tb)
    tb = A[tb].next

# 确保 L1 为较长的链表
if len(L1) < len(L2):
    L1, L2 = L2, L1

# 合并两个链表
c = len(L2) - 1
for i in range(len(L1)):
    ans.append(L1[i])
    if i % 2 == 1 and c >= 0:
        ans.append(L2[c])
        c -= 1

# 打印结果
for i in range(len(ans) - 1):
    print(f"{ans[i]:05d} {A[ans[i]].data} {ans[i+1]:05d}")
print(f"{ans[-1]:05d} {A[ans[-1]].data} -1")
