import math
def fpow(base: int, exponent: int, modulus: int) -> int:
    B = base
    E = exponent
    M = modulus
    result = 1
    while E > 0:
        if E % 2 == 1:
            result *= B % M
        E = math.floor(E / 2)
        B = B ** 2 % M
    return result


if __name__ == "__main__":
    g = 3
    p = 101
    a = 77
    b = 91

    print(fpow(g, a * b, p))
