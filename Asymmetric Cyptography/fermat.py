from random import randint
from math import gcd


def fermat(n, k):
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
    a = 835335 * 2 ** 39014 + 1
    print(fermat(a, 10))