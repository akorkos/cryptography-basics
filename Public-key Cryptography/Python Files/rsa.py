import numpy as np
import gmpy2 as gp
from fpow import fpow


# https://eprint.iacr.org/2023/026.pdf
def fermat(n: int) -> (int, int):
    a = gp.isqrt(n)

    while not gp.is_square(a ** 2 - n):
        a += 1

    bsq = a ** 2 - n
    b = gp.isqrt(bsq)
    p = a + b
    q = a - b
    return int(p), int(q)


# https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/
def inverse_mod(a: int, m: int) -> int:
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return 1


if __name__ == "__main__":
    C = np.array([
        3203, 909, 3143, 5255, 5343,
        3203, 909, 9958, 5278, 5343,
        9958, 5278, 4674, 909, 9958,
        792, 909, 4132, 3143, 9958,
        3203, 5343, 792, 3143, 4443
    ])

    N = 11413
    e = 19

    p, q = fermat(N)
    phi = (p - 1) * (q - 1)
    d = inverse_mod(e, phi)

    m = "".join([chr(fpow(c, d, N)) for c in C])

    print("[01] Decrypted message:", m)



