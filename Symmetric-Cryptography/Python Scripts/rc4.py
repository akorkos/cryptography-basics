import sys

N = 32

ALPHABET = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7,
    'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15,
    'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23,
    'Y': 24, 'Z': 25, '.': 26, '!': 27, '?': 28, '(': 29, ')': 30, '-': 31
}

# https://stackoverflow.com/questions/483666/reverse-invert-a-dictionary-mapping
DIGITS = {
    v: k for k, v in ALPHABET.items()
}


def toDigit(sentence: str) -> list:
    digits = []
    for character in sentence:
        if character in ALPHABET:
            digits.append(ALPHABET[character])
    return digits


def toString(sentence: list) -> str:
    string = ''
    for character in sentence:
        if character in DIGITS:
            string += DIGITS[character]
    return string


def sBoxGeneration(key: list) -> list:
    S = [i for i in range(N)]
    i = 0
    for j in range(N):
        i = (i + S[j] + key[j % len(key)]) % N
        S[j], S[i] = S[i], S[j]
    return S


# https://gist.github.com/hsauers5/491f9dde975f1eaa97103427eda50071
def outputGeneration(S: list):
    i = 0
    j = 0
    while True:
        i = (i + 1) % N
        j = (j + S[i]) % N
        S[j], S[i] = S[i], S[j]
        yield S[(S[i] + S[j]) % N]


def encrypt(message: str, key: str) -> list:
    message = toDigit(message)
    key = toDigit(key)
    S = sBoxGeneration(key)
    K = outputGeneration(S)
    enc = []
    for character in message:
        enc.append(character ^ next(K))
    return enc


def decrypt(cipher: list, key: str) -> list:
    key = toDigit(key)
    S = sBoxGeneration(key)
    K = outputGeneration(S)
    dec = []
    for character in cipher:
        dec.append(character ^ next(K))
    return dec


if __name__ == '__main__':
    message = 'MISTAKES ARE AS SERIOUS AS THE RESULTS THEY CAUSE'
    key = "HOUSE"

    if len(sys.argv) > 2:
        message = str(sys.argv[1])
        key = str(sys.argv[2])

    encrypted = encrypt(message, key)
    print('[1] Encrypted message:', toString(encrypted))

    decrypted = decrypt(encrypted, key)
    print('[2] Decrypted message:', toString(decrypted))
