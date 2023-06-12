import random
from timeit import default_timer as timer
from multiprocessing.pool import Pool
from sympy.ntheory import isprime


def equiv(a: int, b: int, n: int) -> bool:
    return (a % n) == (b % n)


def square_and_multiply(x: int, k: int, p=None) -> int:
    b = bin(k).lstrip('0b')
    r = 1
    for i in b:
        r **= 2
        if i == '1':
            r *= x
        if p:
            r %= p
    return r


def miller_rabin(p: int, s=5) -> bool:
    if not (p & 1):
        return False
    if not equiv(p, 2, 3):
        return False
    if not equiv(p, 3, 4):
        return False

    q = 2 * p + 1

    if not equiv(q, 2, 3):
        return False
    if not equiv(q, 3, 4):
        return False

    p1 = p - 1
    u = 0
    r = p1  # p-1 = 2**u * r

    while r % 2 == 0:
        r >>= 1
        u += 1

    # at this stage p-1 = 2**u * r  holds
    assert p-1 == 2**u * r

    def witness(a):
        """
        Returns: True, if there is a witness that p is not prime.
                False, when p might be prime
        """
        z = square_and_multiply(a, r, p)
        if z == 1:
            return False

        for i in range(u):
            z = square_and_multiply(a, 2**i * r, p)
            if z == p1:
                return False
        return True

    for j in range(s):
        a = random.randrange(2, p-2)
        if witness(a):
            return False

    return True


def generate_primes(min: int, max: int, n=512, k=1) -> list:
    assert k > 0
    assert 0 < n < 4096

    p = random.getrandbits(n)
    while max < p < min:
        p = random.getrandbits(n)

    primes = []

    while k > 0:
        if miller_rabin(p, s=7) and mi:
            primes.append(p)
            k -= 1
        p += 1

    return primes


def main(_):
    data = open("min_max_2048_bit_prime.txt", "r")
    minPrime = int(data.readline())
    maxPrime = int(data.readline())
    n = 2048
    start = timer()
    generate_primes(min=minPrime, max=maxPrime, n=n)
    end = timer()
    return end - start


if __name__ == '__main__':
    processes = 6  # Specify number of processes here
    p = Pool(processes)
    times = p.map(main, range(10))
    failed = 0
    for t in times:
        if t > 180:
            failed += 1
    print("M.O.:", sum(times) / len(times))
    print("Failure percentage:", failed / 100.0)
