def trialDivision(n: int) -> list:
    L = []
    while n % 2 == 0:
        L.append(2)
        n /= 2
    f = 3
    while f ** 2 <= n:
        if n % f == 0:
            L.append(f)
            n /= f
        else:
            f += 2
    if n != 1:
        L.append(n)
    return L


if __name__ == "__main__":
    print("[01] 2 ^ 62 - 1 = ", trialDivision(2 ** 62 - 1))
    print("[02] 2 ^ 102 - 1 = ", trialDivision(2 ** 102 - 1))