from trial_division import trialDivision
from math import floor, ceil, sqrt, gcd
from random import randint
import time
import signal


def timeout_handler(signum, frame):
    raise TimeoutError("Function timed out")


def timeout_function(func, timeout):
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(timeout)

    try:
        result = func()
        signal.alarm(0)  # Cancel the alarm
        return result
    except TimeoutError:
        return None


def randomBinaryNumber(N: int = 100) -> str:
    number = ""
    for _ in range(N):
        number += str(randint(0, 1))
    return number


def lehman(n: int):
    L = trialDivision(n)
    for d in L:
        if d < n ** (1/3):
            return d

    for k in range(1, floor(n ** (1/3)) + 1):
        for a in range(ceil(sqrt(4 * k * n)), floor(sqrt(4 * k * n) + (n ** (1/6)) / (4 * sqrt(k)))):
            b = sqrt(a ** 2 - 4 * k * n)
            if int(b) == b:
                return gcd(a - int(b), n)


if __name__ == "__main__":
    counter = 0

    for _ in range(1000):
        n = randomBinaryNumber()
        ans = timeout_function(lehman(n), 10)


    print(counter)