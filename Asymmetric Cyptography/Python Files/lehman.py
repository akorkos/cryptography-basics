from trial_division import trialDivision
from math import floor, ceil, sqrt, gcd
from random import randint
import time


def randomBinaryNumber(N: int = 100) -> str:
    number = ""
    for _ in range(N):
        number += str(randint(0, 1))
    return number


def lehman(n: int):
    st = time.time()
    L = trialDivision(n)
    for d in L:
        if d < n ** (1/3):
            et = time.time()
            if et - st > 10:
                return -1
            return d

    for k in range(1, floor(n ** (1/3)) + 1):
        for a in range(ceil(sqrt(4 * k * n)), floor(sqrt(4 * k * n) + (n ** (1/6)) / (4 * sqrt(k)))):
            b = sqrt(a ** 2 - 4 * k * n)
            if int(b) == b:
                et = time.time()
                if et - st > 10:
                    return -1
                return gcd(a - int(b), n)


if __name__ == "__main__":
    counter = 0

    for _ in range(1000):
        n = randomBinaryNumber()
        if lehman(int(n, 2)) != 1:
            counter += 1

    print(counter)