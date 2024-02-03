import sys
import random

ALPHABET = {
    'A': '00000', 'B': '00001', 'C': '00010', 'D': '00011', 'E': '00100', 'F': '00101', 'G': '00110', 'H': '00111',
    'I': '01000', 'J': '01001', 'K': '01010', 'L': '01011', 'M': '01100', 'N': '01101', 'O': '01110', 'P': '01111',
    'Q': '10000', 'R': '10001', 'S': '10010', 'T': '10011', 'U': '10100', 'V': '10101', 'W': '10110', 'X': '10111',
    'Y': '11000', 'Z': '11001', '.': '11010', '!': '11011', '?': '11100', '(': '11101', ')': '11110', '-': '11111'
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


def XOR(a: list, b: list) -> list:
    ans = []
    for i in range(len(a)):
        ans.append(f"{int(a[i], 2) ^ int(b[i], 2):05b}")
    return ans


def keyGenerator(length: int) -> str:
    key = ""
    for _ in range(length):
        key += random.choice(list(ALPHABET.keys()))
    return key


def encrypt(message: str, key: str) -> str:
    message = toDigit(message)
    key = toDigit(key)
    return toString(XOR(message, key))


def decrypt(cipher: str, key: str) -> str:
    cipher = toDigit(cipher)
    key = toDigit(key)
    return toString(XOR(cipher, key))


if __name__ == '__main__':
    message = "MISTAKES ARE AS SERIOUS AS THE RESULTS THEY CAUSE"

    if len(sys.argv) > 1:
        message = str(sys.argv[1])

    N = len(message)
    key = keyGenerator(N)

    encrypted = encrypt(message, key)
    print('[1] Encrypted message:', encrypted)

    decrypted = decrypt(encrypted, key)
    print('[2] Decrypted message:', decrypted)
