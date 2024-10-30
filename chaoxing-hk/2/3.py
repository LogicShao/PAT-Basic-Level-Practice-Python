from math import acos, degrees

a = float(input('请输入直角三角形的直角边A(A>0)： '))
b = float(input('请输入直角三角形的直角边B(B>0)： '))
c = (a**2 + b**2)**0.5
print('直角三角形的三边分别为： a={:.1f}, b={:.1f}, c={:.1f}'.format(a, b, c))
print('三角形的周长 = {:.1f}， 面积 = {:.1f}'.format(a+b+c, a*b/2))
angle_A = degrees(acos(b/c))
angle_B = degrees(acos(a/c))
print('三角形的两个锐角的度数分别为：{:.1f} 和 {:.1f}'.format(angle_A, angle_B))
