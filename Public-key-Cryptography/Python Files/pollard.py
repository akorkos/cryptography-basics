from math import gcd
from random import randint


# https://cp-algorithms.com/algebra/factorization.html#implementation
def f(x: int, N: int) -> int:
    return (x ** 2 + 1) % N


def pollard(N: int) -> int:
    x0 = randint(2, N - 1)
    x = x0
    y = x0
    d = 1
    while d == 1:
        x = f(x, N)
        y = f(y, N)
        y = f(y, N)
        d = gcd(abs(x - y), N)
    return d


if __name__ == "__main__":
    N = 2 ** 257 - 1
    print(pollard(N))  # 535006138814359
