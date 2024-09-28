num, inx = input().split("E")
out = "" if num[0] == "+" else "-"
a, de = num[1:].split(".")
num0 = a+de
num_zero = int(inx[1:])
q = len(de)
if num_zero == 0:
    out += num[1:]
elif inx[0] == "+":
    w = num_zero - q
    if w < 0:
        out += num0[:(num_zero+1)] + "." + num0[(num_zero+1):]
    else:
        out += num0 + "0" * w
else:
    out = out + "0." + "0" * (num_zero-1) + num0
print(out)
