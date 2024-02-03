import math
import sys


def primeFactors(n: int) -> list:
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def squaredPrimeFactor(factors: list) -> bool:
    found = False
    for factor in factors:
        if math.isqrt(factor) ** 2 == factor:
            found = True
            break
    return found


def findDivisors(n: int) -> list:
    divisors = []
    for d in range(1, n + 1):
        if n % d == 0:
            divisors.append(d)
    return divisors


def moebius(d: int) -> int:
    factors = primeFactors(d)
    k = len(factors)
    if d == 1:
        return 1
    if squaredPrimeFactor(factors):
        return 0
    return (-1) ** k


if __name__ == '__main__':
    if len(sys.argv) != 1:
        n = int(sys.argv[1])
    else:
        n = 10
    S = sum([moebius(d) * 2 ** (n / d) for d in findDivisors(n)])
    N = S / n
    print("[1] N_2("+str(n)+") =", N)
