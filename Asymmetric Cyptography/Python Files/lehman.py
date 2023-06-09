from trial_division import trialDivision
from random import getrandbits
from gmpy2 import isqrt, is_square, ceil, floor, gcd, sqrt, cbrt


def lehman(n: int):
    cbrtN = cbrt(n)
    sixthRootN = sqrt(cbrtN)
    print(floor(cbrtN))

    for k in range(1, int(floor(cbrtN)) + 1):
        sqrt4kN = sqrt(4 * k * n)
        aStart = int(ceil(sqrt4kN))
        aLimit = int(floor(sqrt4kN + sixthRootN / (4 * sqrt(k))))
        for a in range(aStart, aLimit + 1):
            test = a ** 2 - 4 * k * n
            b = isqrt(test)
            print(b)
            if is_square(b):
                return gcd(a + b, n)
    return 0  # fail


if __name__ == "__main__":
    counter = 0

    for _ in range(10):
        n = getrandbits(100)
        print(n, lehman(n))

