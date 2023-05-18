from math import gcd


def pollard(f, x0, N):
    x = x0
    y = x0
    i = 1
    while i <= N:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x - y), N)
        if 1 < d < N:
            return d
    return None
