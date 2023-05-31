from math import log, e
import os
from concurrent.futures import ProcessPoolExecutor

eg = e ** .577


def sumOfDivisors(n: int):
    sum = 0
    # max_divisor = (n + 1) // 2
    for i in range(n + 1, 1, -1):
        if n % i == 0:
            sum += i
    return sum


def upperBound(n: int) -> float:
    return (eg / 2) * log(log(n)) + .74 / log(log(n))


if __name__ == "__main__":
    N = 2 ** 20
    for n in range(1, N, 2):
        if n != 1:
            if sumOfDivisors(n) / n >= upperBound(n):
                print("Error", n)
