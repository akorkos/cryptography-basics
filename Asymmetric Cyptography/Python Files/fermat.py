from random import randrange
from gmpy2 import gcd


def fermat(p, s=5):
    if p == 2:
        return True
    if not p & 1:  
        return False

    for i in range(s):
        a = randrange(2, p - 2)
        x = pow(a, p - 1, p) 
        if gcd(a, x) > 1:
            return False
        if x != 1:
            return False
    return True


if __name__ == "__main__":
    a = 835335 * 2 ** 39014 + 1  
    b = 835335 * 2 ** 39014 - 1  
    print("[01] Fermat test for {0} returns {1}".format(a, fermat(a)))
    print("[02] Fermat test for {0} returns {1}".format(b, fermat(b)))
