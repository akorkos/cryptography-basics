from random import randint


def createMessage(N: int = 16) -> list:
    return [randint(0, 1) for _ in range(N)]


def shift(msg: list, n: int) -> list:
    return msg[n:] + msg[:n]


def XOR(a: list, b: list) -> list:
    return [a[i] ^ b[i] for i in range(len(a))]


if __name__ == "__main__":
    m = createMessage(16)
    m6 = shift(m, 6)
    m10 = shift(m, 10)
    c = XOR(m, XOR(m6, m10))

    c1 = XOR(c, shift(c, 10))
    c2 = XOR(c1, shift(c1, 2))
    c3 = XOR(c2, shift(c, 14))

    m1 = shift(c3, 2)

    print('[1] Encrypted message:', m)
    print('[2] Decrypted message:', m1)

