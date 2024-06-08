import collections
from math import log, e, prod
import os
from concurrent.futures import ProcessPoolExecutor
from trial_division import trialDivision


def upperBound(n: int) -> float:
    return (e ** .577216 / 2) * log(log(n)) + .74 / log(log(n))


def sigma(n: int) -> int:
    factors = collections.Counter(trialDivision(n))
    powers = [[factor ** i for i in range(count + 1)] for factor, count in factors.items()]
    sumOfPowFactors = [sum(i) for i in powers]
    return int(prod(sumOfPowFactors))


def condition(n) -> None:
    s = sigma(n)
    if s / n >= upperBound(n):
        print("Error", n)


if __name__ == "__main__":
    N = 2 ** 20
    workers = os.cpu_count()
    executor = ProcessPoolExecutor(max_workers=workers)
    results = executor.map(condition, [_ for _ in range(1, N, 2)])
