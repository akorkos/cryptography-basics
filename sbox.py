import numpy as np
import matplotlib.pyplot as plt


S = np.array([
    [0, 2, 3, 7, 9, 12, 15, 7, 6, 15, 15, 1, 7, 3, 1, 0],
    [1, 5, 6, 13, 4, 1, 5, 11, 7, 8, 7, 1, 1, 3, 2, 13],
    [5, 3, 5, 12, 11, 1, 1, 5, 13, 0, 15, 7, 2, 2, 13, 0],
    [3, 12, 3, 11, 2, 2, 2, 4, 6, 5, 5, 0, 4, 3, 1, 0]
])


def XOR(a: list, b: list) -> list:
    N = len(a)
    ans = [0 for _ in range(N)]
    for i in range(N):
        ans[i] = int(a[i]) ^ int(b[i])
    return ans


def feistel(number: list, m: int) -> list:
    i = int(str(number[0]) + str(number[-1]), 2)
    j = int(''.join([str(_) for _ in number[1:-1]]), 2)
    return list(f"{S[i][j]:0{m}b}")


def diff(x: list, z: list, m: int) -> int:
    y = XOR(feistel(XOR(z, x), m), feistel(z, m))
    return int(''.join([str(_) for _ in y]), 2)


def diffOnSBox(n: int, m: int) -> dict:
    N = 2 ** n
    freq = {_: 0 for _ in range(16)}
    for x in range(1, N):
        X = list(f"{x:0{n}b}")
        for z in range(N):
            Z = list(f"{z:0{n}b}")
            Y = diff(X, Z, m)
            freq[Y] += 1
    return freq


if __name__ == '__main__':
    freq = diffOnSBox(6, 4)
    plt.title("Διαφορική ομοιομορφία")
    plt.ylabel("Συχνότητα")
    plt.xlabel("Τιμή")
    plt.plot(freq.keys(), freq.values(), color="r")
    plt.show()
