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
        self.write = lambda s: self.buffer.write(s)
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
def input(): return sys.stdin.readline().rstrip("\r\n")
def write(x): sys.stdout.write(str(x))


n, l, h = map(int, input().split())
data = [tuple(map(int, input().split())) for _ in range(n)]
a, b, c, d = [], [], [], []
for Id, de, cai in data:
    if de < l or cai < l:
        continue
    elif de >= h and cai >= h:
        a.append((-(de + cai), -de, Id))
    elif de >= h:
        b.append((-(de + cai), -de, Id))
    elif de >= cai:
        c.append((-(de + cai), -de, Id))
    else:
        d.append((-(de + cai), -de, Id))

a.sort()
b.sort()
c.sort()
d.sort()
write(f'{len(a) + len(b) + len(c) + len(d)}\n')

for x, y, z in a:
    write(f'{z} {-y} {-x + y}\n')
for x, y, z in b:
    write(f'{z} {-y} {-x + y}\n')
for x, y, z in c:
    write(f'{z} {-y} {-x + y}\n')
for x, y, z in d:
    write(f'{z} {-y} {-x + y}\n')
