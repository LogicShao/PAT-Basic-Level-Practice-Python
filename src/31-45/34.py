import fractions


def to_mixed_fraction(f):
    if f < 0:
        return "(-{})".format(to_mixed_fraction(-f))
    if f.denominator == 1:
        return str(f.numerator)
    if f.numerator == 0:
        return "0"
    if abs(f.numerator) < f.denominator:
        return str(f)
    return "{} {}/{}".format(f.numerator // f.denominator,
                             abs(f.numerator) % f.denominator,
                             f.denominator)


s1, s2 = map(fractions.Fraction, input().split())
for c in "+-*/":
    a = to_mixed_fraction(s1)
    b = to_mixed_fraction(s2)
    ans = to_mixed_fraction(eval("s1{}s2".format(c))
                            ) if c != "/" or s2 != 0 else "Inf"
    print("{} {} {} = {}".format(a, c, b, ans))
