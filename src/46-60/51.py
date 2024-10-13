from cmath import rect

EPS = 1e-4
a, b, c, d = map(float, input().split())
ans = rect(a, b) * rect(c, d)
A = 0 if abs(ans.real) < EPS else ans.real
B = 0 if abs(ans.imag) < EPS else ans.imag
print(f'{A:.2f}{B:+.2f}i')
