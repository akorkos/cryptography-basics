import collections
from trial_division import trialDivision
from fermat import fermat
from sympy.ntheory import factorint


def square_free(primes: dict) -> bool:
    for m in primes.values():
        if m > 1:
            return False
    return True


def korselt(n: int, primes: dict) -> bool:
    for p in primes.keys():
        if ((n-1) % (p-1)) != 0:
            return False
    return n % 2 == 1


def is_carmichael(n: int) -> str:
    primes = factorint(n)  #dict(collections.Counter(trialDivision(n)))
    print(primes)
    print(not fermat(n) , square_free(primes) , korselt(n, primes))
    if not fermat(n) and square_free(primes) and korselt(n, primes):
        return "is Carmichael"
    return "is not Carmichael"


if __name__ == "__main__":
    print("[01] The number: {0}, {1}".format(9999109081, is_carmichael(9999109081)))
    print("[02] The number: {0}, {1}".format(6553130926752006031481761, is_carmichael(6553130926752006031481761)))