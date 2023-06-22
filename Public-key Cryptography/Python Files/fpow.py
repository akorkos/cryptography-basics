from math import floor


def fpow(base: int, exponent: int, modulus: int) -> int:
    B = base
    E = exponent
    M = modulus
    result = 1
    while E > 0:
        if E % 2 == 1:
            result = result * B % M
        E = floor(E / 2)
        B = (B ** 2) % M
    return result


if __name__ == "__main__":
    b = 5
    e = 77
    m = 19

    print("[01] 5 ^ 77 mod 19 = {0}".format(fpow(b, e, m)))
