from random import getrandbits
from sympy import gcd, sqrt, floor, ceiling, primerange
from gmpy2 import is_square, isqrt
import multiprocessing


def trial_division(n: int, limit: int) -> int:
    sieve = primerange(limit)
    for x in sieve:
        if x >= n:
            return x
        if n % x == 0:
            return x


# https://programmingpraxis.com/2017/08/22/lehmans-factoring-algorithm/
def lehman(n: int) -> int:
    s3n = floor(n ** (1 / 3))
    d = trial_division(n, s3n)
    if d < n ** (1/3):
        return d
    for k in range(1, s3n + 1):
        sk = 2 * sqrt(k * n)
        for a in range(ceiling(sk), floor(sk + n ** (1 / 6) / (4 * sqrt(k))) + 1):
            b = a * a - 4 * k * n
            if is_square(b):
                return gcd(a - isqrt(b), n)
    return 0


def call_timeout(timeout, func, args=(), kwargs={}):
    if type(timeout) not in [int, float] or timeout <= 0.0:
        print("Invalid timeout!")

    elif not callable(func):
        print("{} is not callable!".format(type(func)))

    else:
        p = multiprocessing.Process(target=func, args=args, kwargs=kwargs)
        p.start()
        p.join(timeout)

        if p.is_alive():
            p.terminate()
            return False
        else:
            return True


if __name__ == "__main__":
    for _ in range(1000):
        n = getrandbits(100)
        while n % 2 == 0:
            n = getrandbits(100)
        print(call_timeout(10, lehman, args=(n,)))
