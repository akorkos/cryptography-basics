from gmpy2 import isqrt, is_square
import base64
import re


# https://stackoverflow.com/questions/48094595/convert-fraction-to-continued-fraction
def rational_to_continuous_fraction(n: int, d: int) -> list:
    if d == 0:
        return []
    q = n // d
    r = n - q * d
    return [q] + rational_to_continuous_fraction(d, r)


# https://stackoverflow.com/questions/36077810/continued-fractions-python
def continuous_fraction_to_rational(fractions: list) -> (int, int):
    n, d, num, den = 0, 1, 1, 0
    for u in fractions:
        n, d, num, den = num, den, num * u + n, den * u + d
    return num, den


# https://github.com/pablocelayes/rsa-wiener-attack/blob/master/ContinuedFractions.py
def convergents_from_continuous_fraction(fractions: list) -> list:
    return [continuous_fraction_to_rational(fractions[:i]) for i in range(len(fractions))]


def find_d(convergents: list) -> int:
    for (k, d) in convergents:
        if k != 0 and (e * d - 1) % k == 0:
            phi = (e * d - 1) // k
            s = N - phi + 1
            discriminant = s ** 2 - 4 * N
            if discriminant >= 0:
                t = -1
                if is_square(discriminant):
                    t = isqrt(discriminant)
                if t != -1 and (s + t) % 2 == 0:
                    return d


def b64_decode(C: str) -> list:
    base64_bytes = C.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    return re.split('\r\n|,', message_bytes.decode('ascii')[3:-1])


def decrypt(C: list, d: int, N: int) -> str:
    return "".join([chr(pow(int(c), d, N)) for c in C])


if __name__ == "__main__":
    C = open("wiener.txt", "r").read()
    N = 194749497518847283
    e = 50736902528669041

    fractions = rational_to_continuous_fraction(e, N)
    convergents = convergents_from_continuous_fraction(fractions)
    d = find_d(convergents)
    C = b64_decode(C)
    m = decrypt(C, d, N)

    print("[01] Decrypted message: {0}".format(m))
