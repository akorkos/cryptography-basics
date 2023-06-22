from fpow import fpow


if __name__ == "__main__":
    N = 899
    e = 839
    m = 3
    s = 301

    a = fpow(s, e, N)

    print("[01] a = {0} & m = {1}".format(a, m))

