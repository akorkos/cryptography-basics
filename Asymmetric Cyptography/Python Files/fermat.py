from random import randint, randrange
from math import gcd
from sympy.ntheory import isprime


def fermat(n, k = 5):
    i = 1
    j = 0
    while i <= k:
        a = randint(2, n - 1)
        if gcd(a, n) > 1:
            return "Composite", 1
        if pow(a, n - 1, n):
            j += 1
            if j == k:
                return "Prime", 1 - 2 ** (-k)
        i += 1
    return "Composite", 1


if __name__ == "__main__":
    a = 835335 * 2 ** 39014 + 1     # ('Prime', 0.96875)
    b = 835335 * 2 ** 39014 - 1     # ('Prime', 0.96875)
    print(fermat(a))
    print(fermat(b))
