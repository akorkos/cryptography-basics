from fpow import fpow


if __name__ == "__main__":
    p = 101
    g = 3
    a = 77
    b = 91

    Alice = fpow(g, a, p)
    Bob = fpow(g, b, p)

    secretKeyA = fpow(Bob, a, p)
    secretKeyB = fpow(Alice, b, p)

    if secretKeyB == secretKeyA:
        print("[01] Exchange key was successfully calculated!")
        print("[02] Exchange key: ", secretKeyB)
    else:
        print("[01] Exchange key is wrong!")