a, b = map(int, input().split())
clk = (b - a + 50) // 100
h = clk // 3600
m = clk % 3600 // 60
s = clk % 60
print('%02d:%02d:%02d' % (h, m, s))
